# User.urls.py

from django.urls import path
from . import views as User_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', User_views.home, name='User-home'),
    path('User/profile/', User_views.profile, name='User-profile'),
    path('User/register/', User_views.register, name='User-register'),
    path('User/login/', auth_views.LoginView.as_view, name='User-login'),
    path('User/logout/', auth_views.LogoutView.as_view, name='User-logout'),
]