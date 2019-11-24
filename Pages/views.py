from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def admin_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "adminPage.html", {})


def doctor_view(request):
    return render(request, 'doctorPage.html', {'doctors': doctor_view()})


def doctor_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "doctorPage.html", {})

def patient_view(request, *args, **kwargs):
    return render(request, "patientPage.html", {'patients': patient_view()})

def patient_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "patientPage.html", {})


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "contact.html", {})


def forget_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "forgetPassword.html", {})


def news_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "news.html", {})
