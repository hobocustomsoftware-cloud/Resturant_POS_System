from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/tenants/', include('tenants.urls')),
    path('api/users/', include('users.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/purchases/', include('purchases.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/sales/', include('sales.urls')),
    path('api/expenses/', include('expenses.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/billing/', include('billing.urls')),
    path('api/kds/', include('kds.urls')),
]
    path('api/daily/', include('daily.urls')),
    path('api/kds/', include('kds.urls')),
    path('api/daily/', include('daily.urls')),
]
