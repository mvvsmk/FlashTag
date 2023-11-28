from django import forms
from User.models import Vehicle
from django.core.validators import RegexValidator



class VehicleResgisterForm(forms.ModelForm):
    vehicle_number = forms.CharField(max_length=10,validators=[RegexValidator(regex="^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$",
                                                                               message="Enter valid liscence plate number without spaces and specal charecters")])
    vehicle_type = forms.CharField(max_length=10)
    vehicle_model = forms.CharField(max_length=10)
    class Meta:
        model = Vehicle
        fields = ['vehicle_number','vehicle_type','vehicle_model']
