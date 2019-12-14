from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.urls import reverse
from appointments.models import Patient
from django.views.generic import ListView
from appointments.models import Appointment

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


class list_of_patients(ListView):
    model = Patient
    template_name = 'doctorPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PatientModel'] = Patient.objects.all()
        context['my_second_model'] = Patient.objects.all()
        context['my_third_model'] = Patient.objects.all()
        return context

def itemget(request):
        data = Patient.objects.all()
        return render(request, 'doctorPage.html', {'data': data})