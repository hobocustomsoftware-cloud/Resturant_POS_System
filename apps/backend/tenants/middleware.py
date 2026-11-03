from django.utils.deprecation import MiddlewareMixin


class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.tenant = getattr(request.user, 'tenant', None)
        return None
