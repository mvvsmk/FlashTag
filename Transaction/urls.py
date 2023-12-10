# User.urls.py

from django.urls import path
from . import views as Transaction_views
from django.contrib.auth import views as auth_views

app_name = 'Transaction'

urlpatterns = [
    path('test/', Transaction_views.test, name='test'),
    path('transactions/', Transaction_views.TransactionListView.as_view(), name='transactions-list'),
    path('transactions/<int:pk>/', Transaction_views.TransactionDetailView.as_view(), name='Transaction-detail'),
    #create a new transaction
    path('transactions/create/', Transaction_views.NewTransaction, name='Transaction-create'),
    path('toll/<int:toll_id>/', Transaction_views.TollTransactionListView.as_view(), name='Transaction-toll'),
    # path('transaction/<str:username>/', Transaction_views.transaction, name='Transaction-transaction'),
    # path('transaction/<str:username>/<str:vehicle_number>/', Transaction_views.transaction, name='Transaction-transaction'),
    # path('transaction/<str:username>/<str:vehicle_number>/<str:toll_id>/', Transaction_views.transaction, name='Transaction-transaction'),
]