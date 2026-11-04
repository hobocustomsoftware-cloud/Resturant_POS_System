from django.urls import path
from .views import LicenseValidateView, SubscriptionStatusView

urlpatterns = [
    path('license/validate/', LicenseValidateView.as_view()),
    path('subscription/status/', SubscriptionStatusView.as_view()),
]
