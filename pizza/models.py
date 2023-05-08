from django.db import models

# Create your models here.

# Models are used to create tables in the database
# Each class is a table
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings = models.ManyToManyField(Topping)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name