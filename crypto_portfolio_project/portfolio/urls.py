# portfolio/urls.py
from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.holdings_list, name='holdings_list'),
    path('add-to-portfolio/', views.add_to_portfolio, name='add_to_portfolio'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('register/', register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    # Add URL patterns for other views
]

