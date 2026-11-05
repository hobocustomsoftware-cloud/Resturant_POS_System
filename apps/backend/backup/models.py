from django.db import models
from tenants.models import Tenant
from users.models import User


class BackupPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    interval = models.CharField(max_length=20, default='month')
    storage_limit_gb = models.IntegerField(default=5)
    active = models.BooleanField(default=True)


class TenantBackup(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file_path = models.TextField()
    size_bytes = models.BigIntegerField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    downloaded_at = models.DateTimeField(null=True, blank=True)
