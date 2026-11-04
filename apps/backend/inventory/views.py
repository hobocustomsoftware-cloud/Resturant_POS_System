from rest_framework import viewsets
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import Stock, StockMovement
from .serializers import StockSerializer, StockMovementSerializer


class StockViewSet(TenantMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsTenantMember]


class StockMovementViewSet(TenantMixin, viewsets.ReadOnlyModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsTenantMember]
