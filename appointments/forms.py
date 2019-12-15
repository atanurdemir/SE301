from django.forms import ModelForm
from .models import Appointment
from accounts.models import District
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ("patient","Date", "province", "district", "hospital", "clinic", "doctor") # this says to include all fields from model to the form

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district'].queryset = District.objects.none()
            if 'province' in self.data:
                try:
                    province_id = int(self.data.get('province'))
                    self.fields['district'].queryset = District.objects.filter(province_id=province_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['district'].queryset = self.instance.province.district_set.order_by('name')