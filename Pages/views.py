from django.shortcuts import render
from django.http import HttpResponse


def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "register.html", {})
