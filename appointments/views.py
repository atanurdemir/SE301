from django.shortcuts import render
from .models import Appointment, Patient
from django.http import HttpResponse
from .forms import AppointmentForm

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

## PATIENT LISTING AT ADMIN'S SCREEN
class list_of_patients(ListView):

    model = Patient
    template_name = 'appointments/patient_list.html'


##PATIENT LISTING  AT DOCTOR'S SECREEN

class list_of_patients2(ListView):

    model = Patient
    template_name = 'doctorPage.html'

##APPOINTMENT SAVING TO DATABASE

def add_appointment(request):
    if request.method == 'POST':  # data sent by user
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # this will save Car info to database
            return HttpResponse('New appointment added to database')
    else:  # display empty form
        form = AppointmentForm()

    return render(request, 'add_appointment.html', {'appointment_form': form})