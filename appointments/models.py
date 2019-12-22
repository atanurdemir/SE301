from django.db import models
from accounts.models import *



#RANDEVU MODELİ.
#CLINICLER HASTANELERE BAĞLANACAK. SON KALAN İNCE İŞİ BU. 14.12.19
# class Appointment(models.Model):
#     Date = models.DateField()
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     district = models.ForeignKey(District, on_delete=models.CASCADE)
#     province = models.ForeignKey(Province, on_delete=models.CASCADE)
#     clinic = models.ForeignKey(Departments, on_delete=models.CASCADE)
#     hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#        return f'{self.patient}{self.doctor}{self.Date}{self.time}'
#
#     def snippet(self):
#         return self.patient[:15]

class Appointment(models.Model):
    Date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Departments, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)


    def __str__(self):
       return f'{self.patient}{self.doctor}{self.Date}{self.time}'

    def snippet(self):
        return self.patient[:15]
class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    text = models.CharField(max_length=240)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

