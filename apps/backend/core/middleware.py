from django.utils.deprecation import MiddlewareMixin


class LicenseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Enforce license/subscription in standalone/saas modes
        # Placeholder - extend based on APP_MODE
        return None
