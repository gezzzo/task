from unicodedata import category
from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    desciption = models.TextField()
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)