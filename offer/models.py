from django.db import models

# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    # Spurning með þessa að neðan viljum líklega hafa mynd fyrir hvert tilboð og kannski start/end date eða ??
    image = models.ImageField(upload_to='images/')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()