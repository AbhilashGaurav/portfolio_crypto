# portfolio/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .utils import fetch_crypto_data

from .forms import RegistrationForm, AddCryptoForm

from .models import Portfolio

# register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('holdings_list')  # Redirect to home page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy('holdings_list'))  # Redirect to holdings list after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# logout
def user_logout(request):
    logout(request)
    return redirect(reverse('holdings_list'))  # Redirect to the home page after logout

# homepage data
def holdings_list(request):
    crypto_data = fetch_crypto_data()
    holdings = [
        {
            "cryptocurrency": data["name"],
            "image": data["image"],
            "symbol": data["symbol"],
            "current_price": data["current_price"],
            "market_cap": data["market_cap"],
            "market_cap_rank": data["market_cap_rank"],
            "fully_diluted_valuation": data["fully_diluted_valuation"],
            "total_volume": data["total_volume"],
            "high_24h": data["high_24h"],
            "low_24h": data["low_24h"],
            "price_change_24h": data["price_change_24h"],
            "price_change_percentage_24h": data["price_change_percentage_24h"],
            "market_cap_change_24h": data["market_cap_change_24h"],
            "market_cap_change_percentage_24h": data["market_cap_change_percentage_24h"],
            "circulating_supply": data["circulating_supply"],
            "total_supply": data["total_supply"],
            "max_supply": data["max_supply"],
            "ath": data["ath"],
            "ath_change_percentage": data["ath_change_percentage"],
            "ath_date": data["ath_date"],
            "atl": data["atl"],
            "atl_change_percentage": data["atl_change_percentage"],
            "atl_date": data["atl_date"],
            "roi": data["roi"],
            "last_updated": data["last_updated"],
            "purchase_price": 0,
            "purchase_date": None
        } 
        for data in crypto_data
    ]
    return render(request, 'portfolio/holdings_list.html', {'holdings': holdings})


# add new crypto in their portfolio
@login_required
def add_to_portfolio(request):
    if request.method == 'POST':
        form = AddCryptoForm(request.POST)
        if form.is_valid():
            # Create a new Portfolio instance and associate it with the authenticated user
            portfolio = Portfolio(
                user=request.user,
                image = form.cleaned_data['image'],
                cryptocurrency=form.cleaned_data['cryptocurrency'],
                symbol=form.cleaned_data['symbol'],
                quantity=form.cleaned_data['quantity'],
                purchase_price=form.cleaned_data['purchase_price'],
                purchase_date=form.cleaned_data['purchase_date']
            )
            # Save the portfolio instance
            portfolio.save()
            return redirect('portfolio')  # Redirect to holdings list after adding the cryptocurrency
    else:
        form = AddCryptoForm()
    return render(request, 'portfolio/portfolio.html', {'form': form})

# own portfolio
@login_required
def portfolio(request):
    # Retrieve the user's portfolio data
    user_portfolio = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio.html', {'portfolio': user_portfolio})

