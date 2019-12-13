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

###### BU HOSPITAL KULLANILMIYOR BİR ARA SİLECEĞİM. ŞİMDİ SİLİNCE BOZULUYOR.
class Hospital(models.Model):
    province = models.CharField(max_length=200)
    district =models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    numBeds = models.CharField(max_length=5)
    numRooms = models.CharField(max_length=5)

##########################################
class Hospitals(models.Model):
    province = models.CharField(max_length=200)
    district =models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    numBeds = models.CharField(max_length=5)
    numRooms = models.CharField(max_length=5)

class Doctor(models.Model):
    #ID , gsm, address, e-mail, title
    name = models.CharField(max_length=50, default='isim')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}{self.name}{self.gender}{self.gsm}{self.email}{self.address}'

class Patient(models.Model):
    name = models.CharField(max_length=50, default='isim')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)



