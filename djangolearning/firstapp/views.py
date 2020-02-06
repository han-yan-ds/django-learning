from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    templateDict = {'example_template': "Hello I am inserted from the HTML!"}
    return render(req, 'firstapp/index.html', context=templateDict)

def demoUrlMapping(req):
    return HttpResponse("Includes() works!!")