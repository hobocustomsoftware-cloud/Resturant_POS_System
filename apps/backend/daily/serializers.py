from rest_framework import serializers
from .models import DaySession, StockReconciliation


class DaySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaySession
        fields = '__all__'
        read_only_fields = ['tenant', 'opened_by']


class StockReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockReconciliation
        fields = '__all__'
        read_only_fields = ['tenant']
