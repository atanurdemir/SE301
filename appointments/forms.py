from django.forms import ModelForm
from .models import Appointment
from accounts.models import District
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ("Date", "province", "district", "hospital", "clinic", "doctor") # this says to include all fields from model to the form

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district'].queryset = District.objects.none()