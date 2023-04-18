from django.db import models
from datetime import datetime
# Create your models here.

class foods(models.Model):
    food = models.CharField(max_length=50)
    price = models.IntegerField(max_length=5)
    
    def __str__(self):
        return str(self.food)

class drinks(models.Model):
    drink = models.CharField(max_length=50)
    price = models.IntegerField(max_length=5)
    
    def __str__(self):
        return str(self.drink)
class icecreams(models.Model):
    icecream = models.CharField(max_length=50)
    price = models.IntegerField(max_length=5)
    
    def __str__(self):
        return str(self.icecream)