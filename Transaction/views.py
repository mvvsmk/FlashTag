from typing import Any
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from .serializers import TransactionSerializer
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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.base import ContextMixin

# Create your views here.

@api_view(['POST'])
def test(request):
    try :
        data = request.data
        # print(data)
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            print("valid")
            print(data)
            # serializer.save(commit=False)
            message = {
                "status":"200",
                "detail":"Transaction successfull",
                "data" : data
                }
            return Response(message)
        else:
            print("invalid")
            print(serializer.errors)
            message = {
                "status":"400",
                "detail":"Invalid data ",
                "data" : serializer.errors
                }
            return Response(message)

    except Exception as e:
        print(e)

        message = {
            "status":"400",
            "detail":"Invalid data (except)"
            }
        return Response(message)


# list of all transactions
class TransactionListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'Transaction/transaction_list.html'
    context_object_name = "Transactions"
    ordering = ['-transaction_time']
    paginate_by = 5

    def get_queryset(self):
        # get all the transactions
        return Transaction.objects.filter(user=self.request.user).order_by('-transaction_time')
    
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
            profile.save()
            vehicle.vehicle_distance += form.cleaned_data.get("vehicle_distance")
            vehicle.save()
            transaction_amount = fair
            # save user to database
            transaction = form.save(commit=False)
            transaction.transaction_amount = transaction_amount
            transaction.vehicle_number = vehicle
            transaction.save()
            messages.success(request, f'Transaction successfull')
            return redirect('Transaction:transactions-list')
    else:
        form = TransactionCreateForm()
    return render(request, 'Transaction/transaction_form.html', {'form': form})

class TollTransactionListView(UserPassesTestMixin,ListView):
    login_url = 'User:User-login'
    model = Transaction
    template_name = 'Transaction/toll_transaction_list.html'
    context_object_name = 'Transactions'
    ordering = ['-transaction_time']
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff
    
    # def get_queryset(self):
    #     # username=self.kwargs.get('username')
    #     # toll = self.kwargs.get('pk')
    #     toll = get_object_or_404(Toll, id=self.kwargs.get('toll_id'))
    #     queryset = {
    #         "toll":toll,
    #         "transactions":Transaction.objects.filter(toll=toll).order_by('-transaction_time')
    #     }
    #     return queryset
    
    def get_context_data(self):
        context_data = super().get_context_data(**kwargs)
        toll = get_object_or_404(Toll, id=self.kwargs.get('toll_id'))
        context_data['Toll_model'] = toll
        context_data['Transactions'] = Transaction.objects.filter(toll=toll).order_by('-transaction_time')
        return context_data

    

