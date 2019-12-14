from django.conf.urls import url
from . import views
from django.urls import path
from .views import list_of_appointments, list_of_patients, add_appointment
app_name = 'appointments'

urlpatterns=[
    # url(r'^$', views.appointment_list, name="list"),
    # url(r'^(?P<DoctorName>[\w-]+)/$', views.appointment_details, name="detail"),
    # path('appointment_list', list_of_appointments.as_view(), name="appointment_list")
    url(r'^appointment_list/$', list_of_appointments.as_view(), name='list1'),
    url(r'^patient_list/$', list_of_patients.as_view(), name='list2'),
    url(r'add-appointment/$', views.add_appointment, name='add_appointment'),
    path('add/', views.AppointmentCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.AppointmentUpdateView.as_view(), name='person_change'),
]
