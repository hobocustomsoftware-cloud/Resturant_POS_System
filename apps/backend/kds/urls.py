from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KDSViewSet

router = DefaultRouter()
router.register(r'orders', KDSViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
