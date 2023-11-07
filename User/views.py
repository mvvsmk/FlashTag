from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileResgisterForm, VehicleResgisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Vehicle

# Create your views here.

# home page view
def home(request):
    context = {
        'users' : DjangoUser.objects.all()
    }
    return render(request, 'User/home.html',context)

# profile page view
def profile(request):
    return render(request, 'User/profile.html')

# register page view
def register(request):
    if request.method == 'POST':
        form_user = UserRegisterForm(request.POST)
        form_profile = UserProfileResgisterForm(request.POST)
        if form_user.is_valid() and form_profile.is_valid():
            username = form_user.cleaned_data.get("username")
            # save user to database
            user = form_user.save(commit=False)
            profile = form_profile.save(commit=False)
            profile.user = user

            user.save()
            profile.save()
            # flash message
            messages.success(request, f'Account created for {username}!')
            # redirect to home page
            return redirect('User-home')
    else:
        form_user = UserRegisterForm()
        form_profile = UserProfileResgisterForm()
    return render(request, 'User/register.html',{'form_user':form_user, 'form_profile':form_profile})

# vehicles page view
def vehicles(request):
    context = {
        'vehicles' : Vehicle.objects.all()
    }
    return render(request, 'User/vehicles.html',vehicles)

# transactions page view
def transactions(request):
    return render(request, 'User/transactions.html')

#register vehicle    vehicle_type = forms.CharField(max_length=10)
    vehicle_model = forms.CharField(max_length=10)

@login_required
def registerVehicle(request):
    if request.method == 'POST':
        rv_form = VehicleResgisterForm()
        if rv_form.is_valid() :
            vehicle = rv_form.save(commit=False)
            vehicle.vehicle_number = rv_form.cleaned_data.get("vehicle_number")
            vehicle.vehicle_type = rv_form.cleaned_data.get("vehicle_type")
            vehicle.vehicle_model = rv_form.cleaned_data.get("vehicle_model")
            vehicle.vehicle_distance = 0
            vehicle.user = request.user
            vehicle.save()
            # flash message
            messages.success(request, f'Vehicle registered!')
            # redirect to home page
            return redirect('User-home')
        else :
            messages.warning(request, f'Vehicle not registerd!')
    else:
        rv_form = VehicleResgisterForm()
    return render(request, 'User/registerVehicle.html',{'rv_form':rv_form})


