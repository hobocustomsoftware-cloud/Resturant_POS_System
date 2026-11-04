from django.utils.deprecation import MiddlewareMixin


class LicenseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Placeholder for license/subscription enforcement
        return None
