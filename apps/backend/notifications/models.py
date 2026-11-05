from django.db import models
from tenants.models import Tenant
from users.models import User


class DeviceToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='device_tokens')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    token = models.TextField()
    platform = models.CharField(max_length=20, choices=[('web', 'Web'), ('android', 'Android'), ('ios', 'iOS'), ('desktop', 'Desktop')])
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class Notification(models.Model):
    TYPE_CHOICES = (
        ('order', 'Order'),
        ('kds', 'Kitchen'),
        ('stock', 'Stock'),
        ('payment', 'Payment'),
        ('system', 'System'),
    )
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='system')
    data = models.JSONField(null=True, blank=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
