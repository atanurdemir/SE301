from django.conf.urls import url
from . import views
from accounts.views import *
from django.urls import path
from .views import list_of_patient, hospital_list_view
appname = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.register_view, name="signup"),
    url(r'^signup2/$', views.register_view2, name="signup2"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^forgetPassword/$', views.forgotpassword_view, name="forgetPassword"),
    #url(r'^patientPage/$', list_of_patient.as_view(), name='list'),
    url(r'^patientPage/$', hospital_list_view, name='hospitallist')
    # path('forgotpassword',forgotpassword_view, name = "forgot")

]
