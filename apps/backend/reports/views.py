from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from sales.models import Order
from expenses.models import Expense
from purchases.models import Purchase
from decimal import Decimal


class DailySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        date = request.query_params.get('date')
        orders = Order.objects.filter(tenant=tenant)
        if date:
            orders = orders.filter(created_at__date=date)
        sales_total = orders.filter(status='completed').aggregate(s=Sum('total'))['s'] or Decimal(0)
        expenses = Expense.objects.filter(tenant=tenant)
        if date:
            expenses = expenses.filter(date__date=date)
        expenses_total = expenses.aggregate(s=Sum('amount'))['s'] or Decimal(0)
        purchases = Purchase.objects.filter(tenant=tenant)
        if date:
            purchases = purchases.filter(date__date=date)
        purchases_total = purchases.aggregate(s=Sum('total'))['s'] or Decimal(0)
        return Response({
            'date': date,
            'sales_total': float(sales_total),
            'expenses_total': float(expenses_total),
            'purchases_total': float(purchases_total),
            'net': float(sales_total - expenses_total)
        })


class PnLView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = getattr(request, 'tenant', None) or request.user.tenant
        date = request.query_params.get('date')
        orders = Order.objects.filter(tenant=tenant, status='completed')
        if date:
            orders = orders.filter(created_at__date=date)
        revenue = orders.aggregate(s=Sum('total'))['s'] or Decimal(0)
        expenses = Expense.objects.filter(tenant=tenant)
        if date:
            expenses = expenses.filter(date__date=date)
        exp_total = expenses.aggregate(s=Sum('amount'))['s'] or Decimal(0)
        return Response({
            'revenue': float(revenue),
            'expenses': float(exp_total),
            'profit': float(revenue - exp_total)
        })
