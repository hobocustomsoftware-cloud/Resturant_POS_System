from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
        ('sales', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=4, default=0, max_digits=15)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.branch')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.unit')),
            ],
            options={
                'unique_together': {('branch', 'item')},
            },
        ),
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=15)),
                ('type', models.CharField(choices=[('purchase', 'Purchase'), ('sale', 'Sale'), ('adjust', 'Adjust'), ('waste', 'Waste'), ('transfer', 'Transfer')], max_length=20)),
                ('ref_type', models.CharField(blank=True, max_length=50, null=True)),
                ('ref_id', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.branch')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.unit')),
            ],
        ),
    ]
