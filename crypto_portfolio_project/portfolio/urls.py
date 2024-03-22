# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.holdings_list, name='holdings_list'),
    path('add-to-portfolio/', views.add_to_portfolio, name='add_to_portfolio'),
    path('portfolio/', views.portfolio, name='portfolio'),
    # Add URL patterns for other views
]

