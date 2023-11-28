from django.shortcuts import render
from User.models import Vehicle
from .forms import VehicleResgisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User as DjangoUser
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


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
