from django.db import models
from accounts.models import *



#RANDEVU MODELİ.
#CLINICLER HASTANELERE BAĞLANACAK. SON KALAN İNCE İŞİ BU. 14.12.19
class Appointment(models.Model):
    Date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    clinic = models.CharField(max_length=40)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)


    def __str__(self):
       return f'{self.patient}{self.doctor}{self.Date}{self.time}'

    def snippet(self):
        return self.patient[:15]

