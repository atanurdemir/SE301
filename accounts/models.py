from django.contrib.auth.models import AbstractUser, User, Group
from django.db import models

Roles = (
    ('admin', 'ADMIN'),
    ('doctor', 'DOCTOR'),
    ('patient', 'PATIENT'),
    ('visitor', 'VISITOR'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    role = models.CharField(max_length=50, choices=Roles, default='client')



class Province(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name



class District(models.Model):
    name = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




####################################################
#               KULLANILMIYOR. SİLİNCE DB PATLIYOR ANLAMSIZ ŞEKİLDE!!!
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district =models.ForeignKey(District, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    numBeds = models.CharField(max_length=5)
    numRooms = models.CharField(max_length=5)
#####################################################







class Hospitals(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district =models.ForeignKey(District, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    numBeds = models.CharField(max_length=5)
    numRooms = models.CharField(max_length=5)


class Departments(models.Model):
    name = models.CharField(max_length=80)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)


class Doctor(models.Model):
    #ID , gsm, address, e-mail, title
    name = models.CharField(max_length=50, default='isim')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=50, default='isim')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Comment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.CharField(max_length=240)