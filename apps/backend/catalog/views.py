from rest_framework import viewsets
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import Category, Item, Unit, UnitGroup, UnitConversion, ItemRecipe
from .serializers import *


class CategoryViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsTenantMember]


class ItemViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsTenantMember]
    filterset_fields = ['category', 'is_active', 'type']


class UnitGroupViewSet(viewsets.ModelViewSet):
    queryset = UnitGroup.objects.all()
    serializer_class = UnitGroupSerializer
    permission_classes = [IsTenantMember]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsTenantMember]


class UnitConversionViewSet(viewsets.ModelViewSet):
    queryset = UnitConversion.objects.all()
    serializer_class = UnitConversionSerializer
    permission_classes = [IsTenantMember]


class ItemRecipeViewSet(viewsets.ModelViewSet):
    queryset = ItemRecipe.objects.all()
    serializer_class = ItemRecipeSerializer
    permission_classes = [IsTenantMember]
