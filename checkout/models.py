from django.db import models
from django.contrib.auth.models import User
from pizza.models import Pizza

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)