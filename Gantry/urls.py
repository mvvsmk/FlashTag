# Gantry/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# url patterns for Gantry app

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='Gantry/gantry_login.html'), name='gantry-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Gantry/gantry_logout.html'), name='gantry-logout'),
    # path('register/', views.register, name='gantry-register'),
    path('home/', views.home, name='gantry-home'),

]