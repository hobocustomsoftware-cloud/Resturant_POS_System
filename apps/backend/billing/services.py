from django.utils import timezone
from tenants.models import Subscription, Tenant


class SubscriptionService:
    @staticmethod
    def check_subscription(tenant):
        sub = Subscription.objects.filter(tenant=tenant).order_by('-starts_at').first()
        if not sub:
            return {'active': False, 'error': 'No subscription'}
        if sub.status not in ['active', 'trial']:
            return {'active': False, 'error': f'Subscription {sub.status}'}
        if sub.ends_at and sub.ends_at < timezone.now():
            return {'active': False, 'error': 'Subscription expired'}
        return {'active': True, 'subscription': sub, 'plan': sub.plan}

    @staticmethod
    def get_limits(tenant):
        sub = Subscription.objects.filter(tenant=tenant).order_by('-starts_at').first()
        if sub and sub.plan:
            return sub.plan.limits or {}
        return {}
