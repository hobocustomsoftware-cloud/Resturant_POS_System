from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.mixins import TenantMixin
from .models import BackupPlan, TenantBackup
from rest_framework import serializers
from django.core.management import call_command
import os


class BackupPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupPlan
        fields = '__all__'


class TenantBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantBackup
        fields = '__all__'
        read_only_fields = ['tenant']


class BackupPlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BackupPlan.objects.all()
    serializer_class = BackupPlanSerializer
    permission_classes = [IsAuthenticated]


class TenantBackupViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = TenantBackup.objects.all()
    serializer_class = TenantBackupSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def create_backup(self, request):
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        import datetime
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'backup_{tenant.slug}_{timestamp}.sql'
        filepath = f'/tmp/{filename}'
        try:
            call_command('backup_db', output=filepath)
            backup = TenantBackup.objects.create(
                tenant=tenant,
                filename=filename,
                file_path=filepath,
                status='completed'
            )
            return Response(TenantBackupSerializer(backup).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
