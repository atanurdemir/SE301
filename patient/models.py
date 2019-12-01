from django.db import models


class patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_num = models.IntegerField(max_length=11)
    phone_num = models.IntegerField(max_length=11)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)


def __str__(self):
    return self.first_name, self.last_name, self.id_num
