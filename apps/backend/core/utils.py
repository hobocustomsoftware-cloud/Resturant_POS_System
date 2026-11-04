from django.db import models


class TenantQuerySet(models.QuerySet):
    def for_tenant(self, tenant):
        if tenant is None:
            return self.none()
        return self.filter(tenant=tenant)


class TenantManager(models.Manager):
    def get_queryset(self):
        return TenantQuerySet(self.model, using=self._db)

    def for_tenant(self, tenant):
        return self.get_queryset().for_tenant(tenant)


class BaseTenantModel(models.Model):
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)

    class Meta:
        abstract = True
