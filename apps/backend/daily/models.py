from django.db import models
from tenants.models import Tenant
from sales.models import Branch
from users.models import User


class DaySession(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date = models.DateField()
    opened_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='opened_sessions')
    closed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='closed_sessions')
    opening_cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = [['tenant', 'branch', 'date']]
        ordering = ['-date']


class StockReconciliation(models.Model):
    day_session = models.ForeignKey(DaySession, on_delete=models.CASCADE, related_name='reconciliations')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=100)
    item_name = models.CharField(max_length=255)
    system_qty = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    actual_qty = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    difference = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
