from rest_framework import viewsets
from core.mixins import TenantMixin
from core.permissions import IsTenantMember
from .models import ExpenseCategory, Expense
from .serializers import ExpenseCategorySerializer, ExpenseSerializer


class ExpenseCategoryViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsTenantMember]


class ExpenseViewSet(TenantMixin, viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsTenantMember]
    filterset_fields = ['category', 'branch']
