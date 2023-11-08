# User.urls.py

from django.urls import path
from . import views as Transaction_views
from django.contrib.auth import views as auth_views

app_name = 'Transaction'

urlpatterns = [
    path('transactions/', Transaction_views.TransactionListView.as_view(), name='transactions-list'),
    path('transactions/<int:pk>/', Transaction_views.TransactionDetailView.as_view(), name='Transaction-detail'),
    # path('transaction/<str:username>/', Transaction_views.transaction, name='Transaction-transaction'),
    # path('transaction/<str:username>/<str:vehicle_number>/', Transaction_views.transaction, name='Transaction-transaction'),
    # path('transaction/<str:username>/<str:vehicle_number>/<str:toll_id>/', Transaction_views.transaction, name='Transaction-transaction'),
]