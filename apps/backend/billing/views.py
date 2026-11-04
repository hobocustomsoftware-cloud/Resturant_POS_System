from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class LicenseValidateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        license_key = request.data.get('license_key')
        return Response({'valid': bool(license_key), 'message': 'License checked'})


class SubscriptionStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'status': 'active', 'plan': 'basic'})
