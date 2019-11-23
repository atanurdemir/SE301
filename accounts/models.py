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
