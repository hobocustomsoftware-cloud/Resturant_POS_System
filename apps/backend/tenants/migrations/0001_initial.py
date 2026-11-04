# Generated manually
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('interval', models.CharField(default='month', max_length=20)),
                ('features', models.JSONField(blank=True, null=True)),
                ('limits', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('mode', models.CharField(choices=[('standalone', 'Standalone'), ('saas', 'SaaS')], default='standalone', max_length=20)),
                ('status', models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended')], default='active', max_length=20)),
                ('settings', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='trial', max_length=20)),
                ('starts_at', models.DateTimeField(auto_now_add=True)),
                ('ends_at', models.DateTimeField(blank=True, null=True)),
                ('stripe_id', models.CharField(blank=True, max_length=255, null=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.plan')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_key', models.TextField(unique=True)),
                ('issued_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('max_branches', models.IntegerField(default=1)),
                ('max_users', models.IntegerField(default=10)),
                ('features', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=20)),
                ('hardware_id', models.CharField(blank=True, max_length=255, null=True)),
                ('tenant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='license', to='tenants.tenant')),
            ],
        ),
    ]
