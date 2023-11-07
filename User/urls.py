# User.urls.py

from django.urls import path
from . import views as User_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', User_views.home, name='User-home'),
    path('profile/', User_views.profile, name='User-profile'),
    path('register/', User_views.register, name='User-register'),
    path('registerVehicle/', User_views.registerVehicle, name='User-register-vehicle'),
    path('login/', auth_views.LoginView.as_view( template_name = 'User/login.html' ), name='User-login'),
    path('logout/', auth_views.LogoutView.as_view( template_name = 'User/logout.html' ), name='User-logout'),
    path('vehicles/', User_views.vehicles, name='User-vehicles'),
    path('transactions/', User_views.transactions, name='User-transactions'),
]