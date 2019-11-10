from django.db import models

class Appointment(models.Model):
    date = models.DateField()
    time = models.DateTimeField()
    PatientName = models.TextField()
