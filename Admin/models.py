from django.db import models



class Admin(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    userId = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    GSM = models.CharField(max_length=10, unique=True)
    Address = models.CharField(max_length=200)

