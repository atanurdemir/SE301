from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import Patient
from django.comtrib.auth import login,authenticate

def loginPatient(request):
    form  = LoginForm(request.POST or None)

    context = {
        "form":form
    }
