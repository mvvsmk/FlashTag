from django.shortcuts import render
from django.http import HttpResponse
from .models import Toll,Transaction

# Create your views here.
#dummy data for testing
toll_data = [
    {
        'toll_id': 1,
        'toll_name': 'Toll 1',
        'toll_location': 'Location 1',
        'toll_price_collected': 100,
    },
    {
        'toll_id': 2,
        'toll_name': 'Toll 2',
        'toll_location': 'Location 2',
        'toll_price_collected': 200,
    },
    {
        'toll_id': 3,
        'toll_name': 'Toll 3',
        'toll_location': 'Location 3',
        'toll_price_collected': 300,
    },
]

# transaction dummy data for testing
transaction_data = [
    {
        'transaction_id': 1,
        'user': 'User 1',
        'toll_id': 'Toll 1',
        'vehicle_number': 'Vehicle 1',
        'vehicle_distance': 100,
        'transaction_amount': 100,
        'transaction_time': 'April 1, 2021',
    },
    {
        'transaction_id': 2,
        'user': 'User 2',
        'toll_id': 'Toll 2',
        'vehicle_number': 'Vehicle 2',
        'vehicle_distance': 200,
        'transaction_amount': 200,
        'transaction_time': 'April 2, 2021',
    },
    {
        'transaction_id': 3,
        'user': 'User 3',
        'toll_id': 'Toll 3',
        'vehicle_number': 'Vehicle 3',
        'vehicle_distance': 300,
        'transaction_amount': 300,
        'transaction_time': 'April 3, 2021',
    },
]

def home(request):
    Tolls = Toll.objects.all()
    Transactions = Transaction.objects.all()
    context = {
        'Tolls' : Tolls,
        'Transactions' : Transactions 
    }

    return render(request, 'Gantry/home.html', context)

# toll gantry login view
def toll_gantry(request):
    return render(request, 'Gantry/gantry_login.html')

# toll gantry dashbord view
def toll_gantry_dashboard(request):
    return render(request, 'Gantry/gantry_dashboard.html')

# # toll gantry payment view
# def toll_gantry_payment(request):
#     return render(request, 'Gantry/toll_gantry_payment.html')

# #toll gantry admin login view
# def toll_gantry_admin_login(request):
#     return render(request, 'Gantry/toll_gantry_admin_login.html')