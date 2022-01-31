from django import forms
from django.forms import ModelForm

from .models import Customer
from .validators import validate_age

# https://docs.djangoproject.com/en/4.0/topics/forms/
class NewCustomerForm(forms.Form):
    fname = forms.CharField(label='First name', max_length=128, min_length=2, required=True)
    lname = forms.CharField(label='Last name', max_length=128, min_length=2, required=True)
    email = forms.EmailField(label='Email', required=True)
    bday = forms.DateField(label='Birth date', required=True,
                           widget=forms.DateInput(attrs={'type': 'date'}),
                           validators=[validate_age])

# Model forms