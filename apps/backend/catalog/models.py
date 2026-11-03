from django.db import models
from tenants.models import Tenant


class UnitGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    group = models.ForeignKey(UnitGroup, on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10, null=True, blank=True)
    is_base = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UnitConversion(models.Model):
    from_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='conversions_from')
    to_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='conversions_to')
    factor = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        unique_together = [['from_unit', 'to_unit']]


class Category(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    TYPE_CHOICES = (
        ('product', 'Product'),
        ('service', 'Service'),
        ('combo', 'Combo'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    track_stock = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='product')

    def __str__(self):
        return self.name


class ItemUnit(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_units')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)
    is_purchase = models.BooleanField(default=True)
    is_sell = models.BooleanField(default=True)


class ItemRecipe(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='recipes')  # combo item
    raw_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='used_in_recipes')
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
