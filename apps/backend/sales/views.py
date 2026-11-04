from rest_framework import viewsets
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import Branch, Table, Order
from .serializers import BranchSerializer, TableSerializer, OrderSerializer


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
