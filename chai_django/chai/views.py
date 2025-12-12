from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import 
from . import models

# Create your views here.

def chai_details(request):
    return render(request,'chai.html')

def chail_menu(request):
    return HttpResponse(models.chai_menu)

def chail_menu(request):
    return HttpResponse(models.chai_stores)
