from django.db import models

class Patient(models.Model):
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    userId = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    gsm = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=200)

