from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('track_stock', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('product', 'Product'), ('service', 'Service'), ('combo', 'Combo')], default='product', max_length=20)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='UnitGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('symbol', models.CharField(blank=True, max_length=10, null=True)),
                ('is_base', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='catalog.unitgroup')),
            ],
        ),
        migrations.CreateModel(
            name='UnitConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.DecimalField(decimal_places=6, max_digits=15)),
                ('from_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversions_from', to='catalog.unit')),
                ('to_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversions_to', to='catalog.unit')),
            ],
            options={
                'unique_together': {('from_unit', 'to_unit')},
            },
        ),
        migrations.CreateModel(
            name='ItemUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_default', models.BooleanField(default=False)),
                ('is_purchase', models.BooleanField(default=True)),
                ('is_sell', models.BooleanField(default=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_units', to='catalog.item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.unit')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='catalog.item')),
                ('raw_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_in_recipes', to='catalog.item')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.unit')),
            ],
        ),
    ]
