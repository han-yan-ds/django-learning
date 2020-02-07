from django.shortcuts import render
from django.http import HttpResponse
from SecondApp.models import Topic, Webpage, AccessRecord, User
# Create your views here.

def index(req):
    webpagesList = AccessRecord.objects.order_by('date')
    templateDict = {
        'access_records': webpagesList
    }
    # templateDict = {
    #     'help_link_text': 'Example of Rendering Text Template',
    #     'image_link_text': 'Example of Rendering Image Template',
    # }
    return render(req, 'SecondApp/index.html', context=templateDict)


def helpPage(req):
    templateDict = {
        'template_exercise':  "Help Page Text",
    }
    return render(req, 'SecondApp/help.html', context=templateDict)


def imageDemo(req):
    templateDict = {
        'template_exercise':  "Demo-ing Image",
    }
    return render(req, 'SecondApp/imageDemo.html', context=templateDict)


def users(req):
    userList = User.objects.order_by('lname')
    userDict = {'users': userList}
    return render(req, 'SecondApp/users.html', context=userDict)
