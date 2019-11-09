from django.db import models

class Doctor(models.Model):
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    userId = models.IntegerField()
    password = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    gsm = models.IntegerField()
    address = models.CharField(max_length=200)
    workDays = models.DateTimeField(max_length=30)
    workHours = models.DateTimeField(max_length=30)