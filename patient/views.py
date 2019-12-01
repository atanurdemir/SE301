from django.shortcuts import render
from .models import patient


# Create your views here.
def patient_view(request):
    selected_patient = patient.objects.get(id=1)
    return render(request, 'patientPage.html', {'selected_patient':selected_patient })



