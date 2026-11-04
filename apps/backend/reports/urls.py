from django.urls import path
from .views import DailySummaryView, PnLView

urlpatterns = [
    path('daily-summary/', DailySummaryView.as_view()),
    path('pnl/', PnLView.as_view()),
]
