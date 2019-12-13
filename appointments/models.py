from django.db import models
from accounts.models import *


class Appointment(models.Model):
    Date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    district = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    clinic = models.CharField(max_length=40)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)


    def __str__(self):
       return f'{self.patient}{self.doctor}{self.Date}{self.time}'

    def snippet(self):
        return self.patient[:15]
    