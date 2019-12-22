from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm, UserForgotPasswordForm, HospitalsForm, DoctorForm, CommentForm, \
    SendPrescriptionForm
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.urls import reverse, reverse_lazy
from appointments.models import Patient
from .models import Doctor
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from appointments.models import Appointment
from django.contrib import messages


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



##                                                              CREATE VİEWS
def HospitalCreateView(request):
    form = HospitalsForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Hospital Created.')
    context = {'form': form}
    return render(request, "accounts/register_hospital.html", context)


def CommentCreateView(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Comment Sent.')
    context = {'form': form}
    return render(request, "accounts/comment_create.html", context)



def SendPrescriptionView(request):
    form = SendPrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Prescription Sent.')
        form = SendPrescriptionForm(None)
    context = {'form': form}
    return render(request, "accounts/send_prescription.html", context)
  
class DoctorCreateView(CreateView):
    form_class = DoctorForm
    queryset = Doctor.objects.all()
    template_name = 'accounts/register_doctor.html'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

#                                                               DETAIL VİEWS
from django.shortcuts import get_object_or_404



class DoctorDetailView(DetailView):
    template_name = 'appointments/doctors_list.html'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Doctor, id=id_)


    #                                                           UPDATE VIEWS

class DoctorUpdateView(UpdateView):
    form_class = DoctorForm
    queryset = Doctor.objects.all()
    template_name = 'accounts/register_doctor.html'
    success_url = reverse_lazy('appointments:list3')
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Doctor, id=id_)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# HOSPITAL UPDATE VIEW EKLENECEK


#                                                           DELETE VIEWS
class DoctorDeleteView(DeleteView):
    template_name = 'accounts/deleteDoctor.html'
    queryset = Doctor.objects.all()
    success_url = reverse_lazy('appointments:list3')
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Doctor, id=id_)
