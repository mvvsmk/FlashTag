from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Transaction
from Toll.models import Toll
from User.models import Vehicle,Profile
from django.contrib.auth.models import User as DjangoUser
from .forms import TransactionCreateForm
# Create your views here.

# list of all transactions
class TransactionListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'Transaction/transaction_list.html'
    context_object_name = "Transactions"
    ordering = ['-transaction_time']
    paginate_by = 5

    def get_queryset(self):
        # get all the transactions
        return Transaction.objects.all()
    
class TransactionDetailView(LoginRequiredMixin,DetailView):
    model = Transaction

def NewTransaction(request):
    if request.method == 'POST':
        form = TransactionCreateForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            curr_user = form.cleaned_data.get("user")
            curr_profile = Profile.objects.get(user=curr_user)
            curr_Toll = form.cleaned_data.get("toll")
            fair = 10*form.cleaned_data.get("vehicle_distance")
            curr_vehicle = form.cleaned_data.get("vehicle_number")
            vehicle = Vehicle.objects.get(vehicle_number=curr_vehicle)
            if not curr_profile or not curr_Toll or not curr_vehicle:
                messages.warning(request, f'Invalid User or toll or vehicle')
                return redirect('Transaction:Transaction-create')
            if profile.account_balance < fair:
                messages.warning(request, f'Insufficient balance')
                return redirect('Transaction:Transaction-create')
            if profile != curr_profile or vehicle.user != curr_user:
                messages.warning(request, f'Curr User and Vehicle user dont match')
                return redirect('Transaction:Transaction-create')
            profile.account_balance -= fair
            profile.update()
            vehicle.vehicle_distance += form.cleaned_data.get("vehicle_distance")
            vehicle.update()
            transaction_amount = fair
            # save user to database
            transaction = form.save(commit=False)
            transaction.transaction_amount = transaction_amount
            transaction.vehicle = vehicle
            transaction.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('Trascation:transaction-list')
    else:
        form = TransactionCreateForm()
    return render(request, 'Transaction/transaction_form.html', {'form': form})
