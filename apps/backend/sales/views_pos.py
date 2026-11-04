from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from django.utils import timezone
from decimal import Decimal
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from purchases.models import Purchase, PurchaseItem
from inventory.models import Stock, StockMovement
from sales.models import Order, OrderItem
from catalog.models import Item, ItemRecipe


class PurchaseViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = None  # will be added
    permission_classes = [IsTenantMember]

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def receive(self, request, pk=None):
        purchase = self.get_object()
        if purchase.status == 'received':
            return Response({'detail': 'Already received'}, status=status.HTTP_400_BAD_REQUEST)
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        for item in purchase.items.all():
            stock, _ = Stock.objects.get_or_create(
                tenant=tenant,
                branch=purchase.branch,
                item=item.item,
                defaults={'unit': item.unit, 'quantity': 0}
            )
            stock.quantity += item.quantity
            stock.unit = item.unit
            stock.save()
            StockMovement.objects.create(
                tenant=tenant,
                branch=purchase.branch,
                item=item.item,
                unit=item.unit,
                quantity=item.quantity,
                type='purchase',
                ref_type='purchase',
                ref_id=str(purchase.id),
                cost_price=item.unit_price
            )
        purchase.status = 'received'
        purchase.save()
        return Response({'detail': 'Purchase received', 'status': purchase.status})


class OrderViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = None
    permission_classes = [IsTenantMember]
    filterset_fields = ['status', 'type', 'branch']

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
        if order.table:
            order.table.status = 'available'
            order.table.save()
        return Response({'detail': 'Order completed', 'status': order.status})

    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        order = self.get_object()
        return Response({'detail': 'Payment recorded', 'order_id': order.id})
