# portfolio/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Holding

# @login_required
# def holdings_list1(request):
#     holdings = Holding.objects.filter(user=request.user)
#     return render(request, 'portfolio/holdings_list.html', {'holdings': holdings})
from django.shortcuts import render
from .utils import fetch_crypto_data

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


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddCryptoForm
from .models import Portfolio

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

# views.py
from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    # Retrieve the user's portfolio data
    user_portfolio = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio.html', {'portfolio': user_portfolio})
