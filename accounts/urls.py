from django.conf.urls import url
from . import views

appname = 'accounts'
urlpatterns=[
    url(r'^signup/$', views.signup_view, name="signup")
]