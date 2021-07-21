from django.db import models
import random as r
# Create your models here.
class santhosh(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.IntegerField()
    
    

class signin(models.Model):
    uname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()

def __str__(self):
        return santhosh

def __str__(self):
        return signin    
