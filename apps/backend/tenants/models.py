from django.db import models


class Tenant(models.Model):
    MODE_CHOICES = (
        ('standalone', 'Standalone'),
        ('saas', 'SaaS'),
    )
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('suspended', 'Suspended'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='standalone')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    settings = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    interval = models.CharField(max_length=20, default='month')
    features = models.JSONField(null=True, blank=True)
    limits = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='trial')
    starts_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    stripe_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.tenant.name} - {self.plan.name}"


class License(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE, related_name='license')
    license_key = models.TextField(unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    max_branches = models.IntegerField(default=1)
    max_users = models.IntegerField(default=10)
    features = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, default='active')
    hardware_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.tenant.name
