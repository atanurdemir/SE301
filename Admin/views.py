from django.shortcuts import render
from django.http import HttpResponse

def detail(request, userId):
   return HttpResponse("You are looking at to admin ID %s" % userId)