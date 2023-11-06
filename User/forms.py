from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Vehicle
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


## validators
def validate_phone_number(phone):
    if not (phone.isdigit() and len(phone) == 10):
        raise ValidationError(
            _('Value enterd is : %(phone)s . Phone number must be 10 digits'), 
            params={'phone': phone},
            )

def validate_addhar_number_number(addhar):
    if not (addhar.isdigit() and len(addhar) == 10):
        raise ValidationError(
            _('Value entered : %(addhar)s . Addhar number must be 12 digits'), 
            params={'addhar': addhar},
            )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required=True by default
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserProfileResgisterForm(forms.ModelForm):
    addhar_number = forms.CharField(max_length=12)
    phone_number = forms.CharField(max_length=10,validators=[validate_phone_number])

    class Meta:
        model = Profile
        fields = ['addhar_number','phone_number']


class VehicleResgisterForm(forms.ModelForm):
    vehicle_number = forms.CharField(max_length=10)
    vehicle_type = forms.CharField(max_length=10)
    vehicle_model = forms.CharField(max_length=10)

#     class Meta:
#         model = Vehicle
#         fields = [ 'vehicle_id' , 'vehicle_number', 'vehicle_type', 
#                   'vehicle_model']
        