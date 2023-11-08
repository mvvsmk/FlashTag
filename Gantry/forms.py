from . models import Toll,Transaction
from django import forms

class TollRegistrationForm(forms.ModelForm):
    class Meta:
        model = Toll
        fields = ['toll_name','toll_location']