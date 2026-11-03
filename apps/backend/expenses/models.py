from django.db import models
from tenants.models import Tenant
from sales.models import Branch


class ExpenseCategory(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payee = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    receipt_url = models.URLField(null=True, blank=True)
