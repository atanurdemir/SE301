from django.contrib import admin
from django.urls import path
from Pages.views import home_view, register_view, admin_view, doctor_view, patient_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view),
    path('adminPage/', admin_view),
    path('doctorPage/', doctor_view),
    path('patientPage/', patient_view),
    path('admin/', admin.site.urls),
]
