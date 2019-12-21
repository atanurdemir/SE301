from django.forms import ModelForm
from .models import Appointments
from accounts.models import District, Hospitals, Departments, Doctor
from django.http import request
from accounts.models import User

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ("patient", "Date", "province", "district", "hospital", "clinic", "doctor")
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['district'] = District.objects.none()
        self.fields['district'] = District.objects.none()
        self.fields['hospital'] = Hospitals.objects.none()
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province.district_set.order_by('name')