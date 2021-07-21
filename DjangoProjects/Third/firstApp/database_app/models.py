from django.db import models

# Create your models heres
class User_info(models.Model):
    fullname  = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    
    