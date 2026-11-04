from rest_framework import viewsets
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import Supplier, Purchase
from .serializers import SupplierSerializer, PurchaseSerializer


class SupplierViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsTenantMember]


class PurchaseViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsTenantMember]
