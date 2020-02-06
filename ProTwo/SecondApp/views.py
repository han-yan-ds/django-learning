from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    templateDict = {
        'help_link_text': 'Example of Rendering Text Template',
        'image_link_text': 'Example of Rendering Image Template',
    }
    return render(req, 'index.html', context=templateDict)


def helpPage(req):
    templateDict = {
        'template_exercise':  "Help Page Text",
    }
    return render(req, 'help.html', context=templateDict)

def imageDemo(req):
    templateDict = {
        'template_exercise':  "Demo-ing Image",
    }
    return render(req, 'imageDemo.html', context=templateDict)
