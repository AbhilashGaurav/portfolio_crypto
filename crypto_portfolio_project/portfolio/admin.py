from django.contrib import admin
from .models import Holding
from .models import CryptoCurrency
# Register your models here.
admin.site.register(Holding)
admin.site.register(CryptoCurrency)
