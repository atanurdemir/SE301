from django.db import models

class Appointment(models.Model):
    Date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    PatientName = models.CharField(max_length=40)
    DoctorName = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    clinic = models.CharField(max_length=40)
    hospital = models.CharField(max_length=40)
    neighborhood_polyclinic = models.CharField(max_length=40)
    location = models.CharField(max_length=40)


    def __str__(self):
     return self.PatientName, self.DoctorName, self.Date

    def snippet(self):
        return self.PatientName[:15]