from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from django.db import transaction
from .models import Supplier, Purchase
from .serializers import SupplierSerializer, PurchaseSerializer
from inventory.models import Stock, StockMovement


class SupplierViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsTenantMember]


class PurchaseViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
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
        return Response({'detail': 'Purchase received'})
