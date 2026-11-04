from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'unit-groups', UnitGroupViewSet)
router.register(r'units', UnitViewSet)
router.register(r'unit-conversions', UnitConversionViewSet)
router.register(r'recipes', ItemRecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
