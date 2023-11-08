from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from User.models import Profile,Vehicle
from Toll.models import Toll
from .models import Transaction
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#create a new transaction form which checks for the user and the vehicle number and the toll id and the distance calculates the fare and creates a new transaction

class TransactionCreateForm(forms.ModelForm):
    vehicle_number = forms.CharField(max_length=10,validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    class Meta:
        model = Transaction
        fields = ['user', 'toll', 'vehicle_distance', 'transaction_time', 'transaction_status']
