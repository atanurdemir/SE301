from django.contrib import admin
from django.urls import path
from Pages.views import home_view
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]
