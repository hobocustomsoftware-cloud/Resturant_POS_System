from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from sales.models import Order
from sales.serializers import OrderSerializer


class KDSViewSet(TenantMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.filter(status__in=['pending', 'preparing', 'ready'])
    serializer_class = OrderSerializer
    permission_classes = [IsTenantMember]

    @action(detail=True, methods=['post'])
    def mark_preparing(self, request, pk=None):
        order = self.get_object()
        order.status = 'preparing'
        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=['post'])
    def mark_ready(self, request, pk=None):
        order = self.get_object()
        order.status = 'ready'
        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=['post'])
    def mark_served(self, request, pk=None):
        order = self.get_object()
        order.status = 'served'
        order.save()
        return Response(OrderSerializer(order).data)
