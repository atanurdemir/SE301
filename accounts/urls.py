from django.conf.urls import url
from django.urls import path
from . import views
from accounts.views import list_of_patients

appname = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.register_view, name="signup"),
    url(r'^signup2/$', views.register_view2, name="signup2"),
    url(r'^login/$', views.login_view, name="login"),
    # url(r'^$', list_of_patients.as_view(), name="patientList"),
    url(r'itemget/$', views.itemget, {'template_name': 'doctorPage.html'}, name='itemget')

]
