#crypto_portfolio_project\urls.py
from django.contrib import admin
from django.urls import path, include
from portfolio.views import holdings_list
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', include('portfolio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', holdings_list, name='holdings_list'),
]