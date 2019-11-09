from django.db import models

class Doctor(models.Model):
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    userId = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=20)
    TITLE = (
        ('INT', 'Intern'),
        ('PRA', 'Practitioner'),
        ('SPE','Specialist'),
        ('OPE','Operating Surgeon'),
        ('APR','Assistant Professor'),
        ('PRO', 'Professor'),
    )
    title = models.CharField(max_length=1, choices=TITLE)
    email = models.CharField(max_length=30)
    gsm = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=200)
    workDays = models.DateField(max_length=30)
    workHours = models.TimeField(max_length=30)