from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Toll,Transaction
from .forms import TollRegistrationForm


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

# toll gantry register view
def toll_gantry_register(request):
    if request == 'POST':
        form = TollRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # flash message
            messages.success(request, f'Toll registered successfully!')
            return redirect('gantry-home')
        else:
            messages.error(request, f'Please check the form again!')
    else:
        form = TollRegistrationForm()
    return render(request, 'Gantry/toll_gantry_register.html', {'form':form})

# # toll gantry payment view
# def toll_gantry_payment(request):
#     return render(request, 'Gantry/toll_gantry_payment.html')

# #toll gantry admin login view
# def toll_gantry_admin_login(request):
#     return render(request, 'Gantry/toll_gantry_admin_login.html')