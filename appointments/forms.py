from django.forms import ModelForm
from .views import Appointment
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ()  # this says to include all fields from model to the form