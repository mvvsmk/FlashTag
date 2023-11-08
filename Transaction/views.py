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
from django.contrib.auth.models import User as DjangoUser
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
