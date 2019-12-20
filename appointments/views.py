from django.shortcuts import render
from .models import Appointments, Patient, Doctor
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
    model = Appointments
    template_name = 'appointments/appointment_list.html'

class list_of_doctors(ListView):
        model = Doctor
        template_name = 'appointments/doctors_list.html'


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
           appointment = form.save(commit=False)
           appointment.patient = request.user
           return HttpResponse('New appointment added to database')
    else:  # display empty form
        form = AppointmentForm()

    return render(request, 'appointments/add_appointment.html', {'appointment_form': form})



from django.views.generic import ListView, CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
class AppointmentListView(ListView):
    model = Appointments
    context_object_name = 'appointments'


class AppointmentCreateView(CreateView):
    model = Appointments
    fields = ("Date", "province", "district", "hospital", "clinic", "doctor")
    success_url = reverse_lazy('person_changelist')



class AppointmentUpdateView(UpdateView):
    model = Appointments
    fields = ("Date", "province", "district", "hospital", "clinic", "doctor")
    success_url = reverse_lazy('person_changelist')



from accounts.models import District
def load_districts(request):
    province_id = request.GET.get('province')
    districts = District.objects.filter(province_id = province_id).order_by('name')
    return render(request, 'appointments/district_dropdown_list_options.html', {'districts': districts})

