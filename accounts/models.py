from django.contrib.auth.models import AbstractUser, User, Group
from django.db import models
from django.urls import reverse


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


class Hospitals(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    numBeds = models.CharField(max_length=5)
    numRooms = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=80)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    # ID , gsm, address, e-mail, title
    name = models.CharField(max_length=50, default='isim')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=20)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse("")


class Patient(models.Model):
    name = models.CharField(max_length=50, default='isim')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Comments(models.Model):
    doctor = models.CharField(max_length=240)
    patient = models.CharField(max_length=240)
    message = models.TextField()


class Comments(models.Model):
    doctor = models.CharField(max_length=240)
    patient = models.CharField(max_length=240)
    message = models.TextField()

class Prescriptions(models.Model):
    patientName = models.CharField(max_length=50)
    diagnosis = models.CharField(max_length=50)
    recipe = models.TextField()
