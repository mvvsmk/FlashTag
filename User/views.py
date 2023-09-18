from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileResgisterForm


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
            form_user.save()
            #form_profile.save()
            # flash message
            messages.success(request, f'Account created for {username}!')
            # redirect to home page
            return redirect('User-home')
    else:
        form_user = UserRegisterForm()
        form_profile = UserProfileResgisterForm()
    return render(request, 'User/register.html',{'form_user':form_user})

# vehicles page view
def vehicles(request):
    return render(request, 'User/vehicles.html')

# transactions page view
def transactions(request):
    return render(request, 'User/transactions.html')
