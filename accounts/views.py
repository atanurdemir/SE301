from MySQLdb._mysql import connection
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)

from accounts import models
from .forms import UserLoginForm, UserRegisterForm, UserForgotPasswordForm
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import DetailView, ListView
from .models import Patient, Hospital

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        user_groups = list(request.user.groups.values_list('name', flat=True))
        if 'doctor' in user_groups:
            return redirect(reverse('doctor'))
        else:
            return redirect(reverse('patient'))
    context = {
        'form': form,
    }
    return render(request, "accounts/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='doctor')
        user.groups.add(group)
        if next:
            return redirect(next)
        return redirect('login')

    context = {
        'form': form,
    }
    return render(request, "accounts/signup.html", context)


def register_view2(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='patient')
        user.groups.add(group)
        if next:
            return redirect(next)
        return redirect('login')

    context = {
        'form': form,
    }
    return render(request, "accounts/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def send_mail_view(request):
    if request.method == 'POST':
        to = request.POST['recipient_email_address']
        send_mail('Changing Password Request', 'Email body', [to, ])
    return render(request, 'accounts/forgetPassword.html')


def forgotpassword_view(request):
    next = request.GET.get('next')
    form = UserForgotPasswordForm(request.POST or None)
    if form.is_valid():
        send_mail_view()
    context = {
        'form': form,
    }
    return render(request, "accounts/forgetPassword.html", context)


class list_of_patient(ListView):
    model = Patient
    template_name = 'patientPage.html'


def hospital_list_view(request):
    queryset= Hospital.objects.all()
    context = {
        "hospital_list": queryset
    }
    return render(request, "patientPage.html", context)