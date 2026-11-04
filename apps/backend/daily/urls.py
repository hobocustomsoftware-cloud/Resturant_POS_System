from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DaySessionViewSet, StockReconciliationViewSet

router = DefaultRouter()
router.register(r'sessions', DaySessionViewSet)
router.register(r'reconciliations', StockReconciliationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
