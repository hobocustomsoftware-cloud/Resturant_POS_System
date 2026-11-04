from rest_framework import permissions
from billing.services import SubscriptionService
from billing.utils import LicenseManager
from django.conf import settings


class CheckLicenseOrSubscription(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        tenant = getattr(request.user, 'tenant', None)
        if not tenant:
            return True
        
        app_mode = getattr(settings, 'APP_MODE', 'standalone')
        
        if app_mode == 'standalone':
            license = getattr(tenant, 'license', None)
            if not license:
                return False
            result = LicenseManager.validate_license(license.license_key)
            return result.get('valid', False)
        elif app_mode == 'saas':
            result = SubscriptionService.check_subscription(tenant)
            return result.get('active', False)
        return True
