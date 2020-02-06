from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse("BABY ONE MORE TIME")

def demoUrlMapping(req):
    return HttpResponse("Includes() works!!")