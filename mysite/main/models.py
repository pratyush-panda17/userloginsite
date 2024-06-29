from django.db import models

# Create your models here.
class User(models.Model): #User model
    is_doctor = models.BooleanField()
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    address = models.CharField(max_length=200)
