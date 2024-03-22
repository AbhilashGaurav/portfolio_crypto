# portfolio/models.py
from django.db import models
from django.contrib.auth.models import User

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name


from django.db import models

class Holding(models.Model):
    cryptocurrency = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=20, decimal_places=5)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.cryptocurrency} - {self.quantity}"

from django.db import models

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    cryptocurrency = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()


    def __str__(self):
        return f"{self.cryptocurrency} - {self.quantity}"