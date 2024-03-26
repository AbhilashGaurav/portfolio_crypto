# portfolio/forms.py

from django import forms
from django.contrib.auth.models import User

# forms.py
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AddCryptoForm(forms.Form):
    image = forms.CharField(label='image')
    cryptocurrency = forms.CharField(label='Cryptocurrency Name')
    symbol = forms.CharField(label='Symbol')
    quantity = forms.DecimalField(label='Quantity')
    purchase_price = forms.DecimalField(label='Purchase Price')
    purchase_date = forms.DateField(label='Purchase Date')
