from django.shortcuts import render
from django.http import HttpResponse


def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {})

def register_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "register.html", {})

def admin_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "adminPage.html", {})

def doctor_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "doctorPage.html", {})

def patient_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "patientPage.html", {})