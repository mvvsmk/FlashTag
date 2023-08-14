from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home page view
def home(request):
    return render(request, 'User/home.html')

# profile page view
def profile(request):
    return render(request, 'User/profile.html')

# register page view
def register(request):
    return render(request, 'User/register.html')