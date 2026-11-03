from django.db import models
from tenants.models import Tenant
from catalog.models import Item, Unit
from sales.models import Branch


class Stock(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=4, default=0)

    class Meta:
        unique_together = [['branch', 'item']]


class StockMovement(models.Model):
    TYPE_CHOICES = (
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
        ('adjust', 'Adjust'),
        ('waste', 'Waste'),
        ('transfer', 'Transfer'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    ref_type = models.CharField(max_length=50, null=True, blank=True)
    ref_id = models.CharField(max_length=100, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
