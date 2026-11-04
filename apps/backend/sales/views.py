from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from django.db import transaction
from .models import Branch, Table, Order, OrderItem
from .serializers import BranchSerializer, TableSerializer, OrderSerializer
from inventory.models import Stock, StockMovement
from catalog.models import Item


class BranchViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsTenantMember]


class TableViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsTenantMember]


class OrderViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsTenantMember]
    filterset_fields = ['status', 'type', 'branch']

    def perform_create(self, serializer):
        tenant = getattr(self.request, 'tenant', None) or self.request.user.tenant
        branch = self.request.data.get('branch') or getattr(self.request.user, 'branch_id')
        if branch and isinstance(branch, str):
            pass
        order_no = self.request.data.get('order_no') or f'ORD-{Order.objects.count()+1:06d}'
        serializer.save(tenant=tenant, user=self.request.user, order_no=order_no, branch_id=branch)

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def add_items(self, request, pk=None):
        order = self.get_object()
        items = request.data.get('items', [])
        for it in items:
            item = Item.objects.get(id=it['item_id'])
            OrderItem.objects.create(
                order=order,
                item=item,
                quantity=it.get('qty', 1),
                unit_id=it.get('unit_id'),
                price=it.get('price', item.price),
                total=it.get('price', item.price) * it.get('qty', 1)
            )
        return Response({'detail': 'Items added'})

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def complete(self, request, pk=None):
        order = self.get_object()
        if order.status == 'completed':
            return Response({'detail': 'Already completed'}, status=status.HTTP_400_BAD_REQUEST)
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        for order_item in order.items.all():
            item = order_item.item
            if item.type == 'combo' and item.track_stock:
                for recipe in item.recipes.all():
                    qty_needed = recipe.quantity * order_item.quantity
                    stock, _ = Stock.objects.get_or_create(
                        tenant=tenant,
                        branch=order.branch,
                        item=recipe.raw_item,
                        defaults={'unit': recipe.unit, 'quantity': 0}
                    )
                    if stock.quantity < qty_needed:
                        return Response({'detail': f'Insufficient stock for {recipe.raw_item.name}'}, status=status.HTTP_400_BAD_REQUEST)
                    stock.quantity -= qty_needed
                    stock.save()
                    StockMovement.objects.create(
                        tenant=tenant,
                        branch=order.branch,
                        item=recipe.raw_item,
                        unit=recipe.unit,
                        quantity=-qty_needed,
                        type='sale',
                        ref_type='order',
                        ref_id=str(order.id)
                    )
            elif item.track_stock:
                stock, _ = Stock.objects.get_or_create(
                    tenant=tenant,
                    branch=order.branch,
                    item=item,
                    defaults={'unit': order_item.unit, 'quantity': 0}
                )
                if stock.quantity < order_item.quantity:
                    return Response({'detail': f'Insufficient stock for {item.name}'}, status=status.HTTP_400_BAD_REQUEST)
                stock.quantity -= order_item.quantity
                stock.save()
                StockMovement.objects.create(
                    tenant=tenant,
                    branch=order.branch,
                    item=item,
                    unit=order_item.unit,
                    quantity=-order_item.quantity,
                    type='sale',
                    ref_type='order',
                    ref_id=str(order.id)
                )
        order.status = 'completed'
        order.save()
        if order.table_id:
            try:
                order.table.status = 'available'
                order.table.save()
            except Exception:
                pass
        return Response({'detail': 'Order completed', 'status': order.status})

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        order = self.get_object()
        order.status = 'paid'
        order.save()
        return Response({'detail': 'Payment recorded', 'order_id': order.id})
