from django.shortcuts import render
from django.http import HttpResponse
from .models import Toll,Transaction

# Create your views here.

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