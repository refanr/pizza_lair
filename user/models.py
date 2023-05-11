from django.contrib.auth.models import User
from django.db import models

from pizza.models import Pizza


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  favorite_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
  profile_image = models.CharField(max_length=9999)
