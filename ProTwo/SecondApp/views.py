from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(req):


def help(req):
    templateDict = {
        'template_exercise':  "Help Page Text"
    }
    return render(req, 'index.html', context=templateDict)