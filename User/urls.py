# User.urls.py

from django.urls import path
from . import views as User_views
from .views import (
    VehicleListView,
)
from django.contrib.auth import views as auth_views

app_name = 'User'

urlpatterns = [
    path('', User_views.landing, name='User-landing'),
    path('ViewAllProfiles/', User_views.home, name='User-lists'),
    path('Profile/<int:pk>/', User_views.ProfileDetailView.as_view(), name='User-profile'),
    path('vehicle/<str:pk>/', User_views.VehicleDetailView.as_view(), name='User-vehicle-detail'),
    path('user/vehicles/<str:username>/', VehicleListView.as_view(), name='User-vehicles'),
    path('UpdateProfile/', User_views.profile, name='User-profile-update'),
    path('register/', User_views.registerUserView, name='User-register'),
    path('registerVehicle/', User_views.registerVehicleView, name='User-register-vehicle'),
    path('login/', auth_views.LoginView.as_view( template_name = 'User/login.html' ), name='User-login'),
    path('logout/', auth_views.LogoutView.as_view( template_name = 'User/logout.html' ), name='User-logout'),
    path('addmoney/', User_views.addMoney, name='User-add-money'),
    # path('user/str/<str:username>/', User_views.about, name='User-about'),
    # path('user/vehicles/<str:username>/update/<str:vehicle_number>/', User_views.VehicleUpdateView.as_view(), name='User-vehicle-update'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('transactions/', User_views.transactions, name='User-transactions'),
]