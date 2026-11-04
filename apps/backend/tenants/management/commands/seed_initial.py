from django.core.management.base import BaseCommand
from tenants.models import Tenant, Plan
from users.models import Role


class Command(BaseCommand):
    help = 'Seed initial data'

    def handle(self, *args, **options):
        plan, _ = Plan.objects.get_or_create(name='Basic', defaults={'price': 0, 'interval': 'month'})
        tenant, _ = Tenant.objects.get_or_create(slug='demo', defaults={'name': 'Demo Restaurant', 'mode': 'standalone'})
        Role.objects.get_or_create(tenant=tenant, name='Admin', defaults={'permissions': {'all': True}})
        Role.objects.get_or_create(tenant=tenant, name='Cashier', defaults={'permissions': {'pos': True}})
        Role.objects.get_or_create(tenant=tenant, name='Kitchen', defaults={'permissions': {'kds': True}})
        self.stdout.write(self.style.SUCCESS('Seeded initial data'))
