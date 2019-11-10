from django.conf.urls import url
from . import views

app_name = 'appointments'

urlpatterns=[
    url(r'^$', views.appointment_list, name="list"),
    url(r'^(?P<DoctorName>[\w-]+)/$', views.appointment_details, name="detail"),
]
