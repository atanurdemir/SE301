from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm, UserForgotPasswordForm, HospitalsForm, DoctorForm, CommentForm, UserRegisterForm2, SendPrescriptionForm,\
    DepartmentForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.urls import reverse, reverse_lazy
from appointments.models import Patient
from django.http import HttpResponseRedirect
from .models import Doctor, Comments, Hospitals, Prescription, Departments
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from appointments.models import Appointment
from django.contrib.messages.views import SuccessMessageMixin


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
        if 'patient' in user_groups:
            return redirect(reverse('patient'))
    context = {
        'form': form,
    }
    return render(request, "accounts/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm2(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='doctor')
        user.groups.add(group)
        if next:
            return redirect(next)
        return redirect('admin')

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


## ######  ######  ######  ######  ######  ######       CREATE VİEWS        ######  ######  ######  ######  ######  ######  ######
class HospitalCreateView(SuccessMessageMixin, CreateView):
    form_class = HospitalsForm
    queryset = Hospitals.objects.all()
    template_name = 'accounts/register_hospital.html'
    success_url = reverse_lazy('admin')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    success_message = "Hospital %(name) saved successfully."


class CommentCreateView(SuccessMessageMixin,CreateView):
    model = Comments
    fields = ("doctor","message")
    success_url = reverse_lazy('patient')
    template_name = 'accounts/comment_create.html'

    def user(request):
        Comments.patient = request.user()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    success_message = "Your comment sent successfully."
class SendPrescriptionView(SuccessMessageMixin, CreateView):
    form_class = SendPrescriptionForm
    queryset = Prescription.objects.all()
    template_name = 'accounts/send_prescription.html'
    success_url = reverse_lazy('send_prescription')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    success_message = "Prescription sent successfully"


class DoctorCreateView(SuccessMessageMixin, CreateView):
    form_class = DoctorForm
    queryset = Doctor.objects.all()
    template_name = 'accounts/register_doctor.html'
    success_url = reverse_lazy('appointments:list3')
    success_message = "Doctor %(name) saved successfully."

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DepartmentCreateView(CreateView, SuccessMessageMixin):

    form_class = DepartmentForm
    queryset = Departments.objects.all()
    template_name = 'accounts/create_department.html'
    success_url = reverse_lazy('admin')
    success_message = "Department %name saved successfully."

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

######  ######  ######  ######  ######  ######     DETAIL VİEWS         ######  ######  ######  ######  ######  ######
from django.shortcuts import get_object_or_404


class DoctorDetailView(DetailView):
    template_name = 'appointments/doctors_list.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Doctor, id=id_)


class HospitalDetailView(DetailView):
    template_name = 'appointments/hospital_list.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Hospitals, id=id_)



###### ######  ######  ######  ######  ######            UPDATE VIEWS            ######  ######  ######  ######  ######

class DoctorUpdateView(SuccessMessageMixin, UpdateView):
    form_class = DoctorForm
    queryset = Doctor.objects.all()
    template_name = 'accounts/register_doctor.html'
    success_url = reverse_lazy('appointments:list3')
    success_message = "Doctor updated successfully."

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Doctor, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

#
class HospitalUpdateView(UpdateView):
    form_class = HospitalsForm
    queryset = Hospitals.objects.all()
    template_name = 'accounts/register_hospital.html'
    success_url = reverse_lazy('appointments:list7')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Hospitals, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# class PatientUpdateView(UpdateView):
#     form_class = PatientForm
    # template_name = 'accounts/register_patient.html'
    # success_url = reverse_lazy('patient')
    #
    # def get_object(self):
    #     id_ = self.request.user
    #
    #     return get_object_or_404(Patient, id=id_)
    #
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


#  ######  ######  ######  ######  ######  ######            DELETE VIEWS          ######  ######  ######  ######  ######
class DoctorDeleteView(DeleteView):
    template_name = 'accounts/deleteDoctor.html'
    queryset = Doctor.objects.all()
    success_url = reverse_lazy('appointments:list3')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Doctor, id=id_)
      
class HospitalDeleteView(DeleteView):
    template_name = 'accounts/delete_hospital.html'
    queryset = Hospitals.objects.all()
    success_url = reverse_lazy('appointments:list7')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Hospitals, id=id_)
@login_required()
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.patient)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('patient')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.patient)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'accounts/profile.html', context)