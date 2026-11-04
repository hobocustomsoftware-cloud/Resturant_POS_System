from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import DaySession, StockReconciliation
from .serializers import DaySessionSerializer, StockReconciliationSerializer
from django.utils import timezone


class DaySessionViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = DaySession.objects.all()
    serializer_class = DaySessionSerializer
    permission_classes = [IsTenantMember]

    @action(detail=False, methods=['get'])
    def current(self, request):
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        today = timezone.now().date()
        session = DaySession.objects.filter(tenant=tenant, date=today, status='open').first()
        if not session:
            return Response({'status': 'closed', 'session': None})
        return Response({'status': 'open', 'session': DaySessionSerializer(session).data})

    @action(detail=False, methods=['post'])
    def open(self, request):
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        branch_id = request.data.get('branch')
        opening_cash = request.data.get('opening_cash', 0)
        today = timezone.now().date()
        session, created = DaySession.objects.get_or_create(
            tenant=tenant,
            branch_id=branch_id,
            date=today,
            defaults={'opened_by': request.user, 'opening_cash': opening_cash, 'status': 'open'}
        )
        return Response(DaySessionSerializer(session).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        session = self.get_object()
        session.status = 'closed'
        session.closed_by = request.user
        session.closed_at = timezone.now()
        session.save()
        return Response(DaySessionSerializer(session).data)


class StockReconciliationViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = StockReconciliation.objects.all()
    serializer_class = StockReconciliationSerializer
    permission_classes = [IsTenantMember]
