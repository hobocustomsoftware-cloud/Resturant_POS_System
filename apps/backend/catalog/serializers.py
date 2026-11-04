from rest_framework import serializers
from .models import Category, Item, Unit, UnitGroup, UnitConversion, ItemUnit, ItemRecipe


class UnitGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitGroup
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitConversion
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['tenant']


class ItemUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemUnit
        fields = '__all__'


class ItemRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecipe
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    item_units = ItemUnitSerializer(many=True, read_only=True)
    recipes = ItemRecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['tenant']
