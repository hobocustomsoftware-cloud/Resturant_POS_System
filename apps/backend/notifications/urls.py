from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, DeviceTokenViewSet

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'devices', DeviceTokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
