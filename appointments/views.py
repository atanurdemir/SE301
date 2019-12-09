from django.shortcuts import render
from .models import Appointment, Patient
from django.http import HttpResponse

# def appointment_list(request):
#  appointments = Appointment.objects.all().order_by('PatientName');
#  return render(request, 'appointments/appointment_list.html', {'appointments':appointments})
#
# def appointment_details(request, PatientName):
#     appointment = Appointment.objects.get(PatientName=PatientName)
#     return render(request, 'appointments/appointment_detail.html', {'appointment':appointment})

from django.views.generic import DetailView, ListView


class list_of_appointments(ListView):

    # queryset = Appointment.objects.all()
    model = Appointment
    template_name = 'appointments/appointment_list.html'


class list_of_patients(ListView):

    model = Patient
    template_name = 'appointments/patient_list.html'

class list_of_patients2(ListView):

    model = Patient
    template_name = 'doctorPage.html'
