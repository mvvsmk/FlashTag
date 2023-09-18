from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required=True by default
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserProfileResgisterForm(forms.ModelForm):
    addhar_number = forms.CharField(max_length=12)
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = Profile
        fields = ['addhar_number','phone_number']
