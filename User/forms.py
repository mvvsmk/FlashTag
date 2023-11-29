from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Vehicle
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


## validators
def validate_phone_number(phone):
    if not (phone.isdigit() and len(phone) == 10):
        raise ValidationError(
            _('Value enterd is : %(phone)s . Phone number must be 10 digits'), 
            params={'phone': phone},
            )

def validate_aadhar_number_number(aadhar):
    if not (aadhar.isdigit() and len(aadhar) == 10):
        raise ValidationError(
            _('Value entered : %(aadhar)s . Aadhar number must be 12 digits'), 
            params={'aadhar': aadhar},
            )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required=True by default
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserProfileResgisterForm(forms.ModelForm):
    aadhar_number = forms.CharField(max_length=12)
    phone_number = forms.CharField(max_length=10,validators=[validate_phone_number])

    class Meta:
        model = Profile
        fields = ['aadhar_number','phone_number']

#vehicle register form for the registration of the vehiclepage
class VehicleResgisterForm(forms.ModelForm):
    vehicle_number = forms.CharField(max_length=10,validators=[RegexValidator(regex="^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$",
                                                                               message="Enter valid liscence plate number without spaces and specal charecters")])
    vehicle_type = forms.CharField(max_length=10)
    vehicle_model = forms.CharField(max_length=10)
    class Meta:
        model = Vehicle
        fields = ['vehicle_number','vehicle_type','vehicle_model']

# for the profile page

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['aadhar_number','phone_number']

class AddFundsForm(forms.Form):
    amount = forms.IntegerField(min_value=10,max_value=10000)

    class Meta:
        fields = ['amount']

    
