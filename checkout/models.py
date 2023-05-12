from django.db import models
from django.contrib.auth.models import User
from pizza.models import Pizza

# Create your models here.
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    credit_card = models.CharField(max_length=16, blank=True)
    pizzas = models.ManyToManyField(Pizza)
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
