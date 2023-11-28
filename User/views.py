from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileResgisterForm, VehicleResgisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Profile, Vehicle


# Create your views here.

# home page view
def home(request):
    context = {
        'profiles' : Profile.objects.all(),
    }
    return render(request, 'User/home.html',context)

# profile page view
@login_required
def profile(request):
    """docstring for profile."""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            # save the user
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('User-profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'User/profile.html',context)

# register page view
def registerUserView(request):
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
            return redirect('User-profile')
    else:
        form_user = UserRegisterForm()
        form_profile = UserProfileResgisterForm()
    return render(request, 'User/register.html',{'form_user':form_user, 'form_profile':form_profile})


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'User/vehicles.html' 
    context_object_name = "vehicles"
    paginate_by = 5 #pagination
    login_url = 'User-login'

    def get_queryset(self):
        curr_user = get_object_or_404(DjangoUser, username=self.kwargs.get('username'))
        return Vehicle.objects.filter(user=curr_user).order_by('-vehicle_number')
    
class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    login_url = 'User-login'

    def get_queryset(self):
        curr_vehicle = get_object_or_404(DjangoUser, username=self.kwargs.get('pk'))
        return Vehicle.objects.filter(vehicle_number=curr_vehicle)

@login_required
def registerVehicleView(request):
    login_url = 'User-login'
    if request.method == 'POST':
        rv_form = VehicleResgisterForm(request.POST)
        if rv_form.is_valid() :
            vehicle = rv_form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            # flash message
            messages.success(request, f'Vehicle registered!')
            # redirect to home page
            return redirect('User-vehicles')
        else :
            messages.warning(request, f'Vehicle not registerd!')
    else:
        rv_form = VehicleResgisterForm()
    return render(request, 'User/registerVehicle.html',{'rv_form':rv_form})

# class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Vehicle
#     fields = ['vehicle_number', 'vehicle_type', 'vehicle_model']
#     template_name = 'User/vehicle_update.html'
#     login_url = 'User-login'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     def test_func(self) -> Any:
#         vehicle = self.get_object()
#         if self.request.user == vehicle.user:
#             return True
#         return False

# transactions page view
# def transactions(request):
#     return render(request, 'User/transactions.html')


# vehicles page view
# def vehiclesView(request):
#     login_required = True
#     login_url = 'User-login'
#     vehicles = {
#         'vehilces' : Vehicle.objects.all()
#     }
#     return render(request, 'User/vehicles.html',vehicles)


