# portfolio/forms.py

from django import forms

class AddCryptoForm(forms.Form):
    image = forms.CharField(label='image')
    cryptocurrency = forms.CharField(label='Cryptocurrency Name')
    symbol = forms.CharField(label='Symbol')
    quantity = forms.DecimalField(label='Quantity')
    purchase_price = forms.DecimalField(label='Purchase Price')
    purchase_date = forms.DateField(label='Purchase Date')
