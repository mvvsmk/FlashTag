# Vehicles.urls.py

from django.urls import path
from . import views as Vehicle_views
from django.contrib.auth import views as auth_views

app_name = 'Vechicle'

urlpatterns = [
    # path('test/', Transaction_views.test, name='test'),
    path('transactions/', Vehicle_views.VehicleListView.as_view(), name='transactions-list'),
    # path('transactions/<int:pk>/', Transaction_views.TransactionDetailView.as_view(), name='Transaction-detail'),
    # #create a new transaction
    # path('transactions/create/', Transaction_views.NewTransaction, name='Transaction-create'),
    # path('transaction/<str:username>/', Transaction_views.transaction, name='Transaction-transaction'),
    # path('transaction/<str:username>/<str:vehicle_number>/', Transaction_views.transaction, name='Transaction-transaction'),
    # path('transaction/<str:username>/<str:vehicle_number>/<str:toll_id>/', Transaction_views.transaction, name='Transaction-transaction'),
]