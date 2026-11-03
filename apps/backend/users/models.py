from django.contrib.auth.models import AbstractUser
from django.db import models
from tenants.models import Tenant


class Role(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    permissions = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey('sales.Branch', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
