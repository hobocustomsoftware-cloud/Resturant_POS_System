from django.utils.deprecation import MiddlewareMixin


class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tenant = None
        # Try header
        tenant_slug = request.headers.get('X-Tenant-Slug') or request.META.get('HTTP_X_TENANT_SLUG')
        if tenant_slug:
            from tenants.models import Tenant
            try:
                tenant = Tenant.objects.filter(slug=tenant_slug, status='active').first()
            except Exception:
                tenant = None
        # Try authenticated user
        if not tenant and hasattr(request, 'user') and request.user.is_authenticated:
            tenant = getattr(request.user, 'tenant', None)
        request.tenant = tenant
        return None
