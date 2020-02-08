from django.shortcuts import render
from django.http import HttpResponse
from SecondApp.models import Topic, Webpage, AccessRecord, User
from SecondApp.forms import FormModel
# Create your views here.

def index(req):
    webpagesList = AccessRecord.objects.order_by('date')
    templateDict = {
        'access_records': webpagesList
    }
    return render(req, 'SecondApp/index.html', context=templateDict)


def form_name_view(req):
    formInstance = FormModel()
    templateDict = {
        'form': formInstance
    }
    if req.method == "POST":
        formInstance = FormModel(req.POST) # 
        if formInstance.is_valid():
            print(formInstance.cleaned_data) # DEMO: Getting data from form upon submit
    return render(req, 'SecondApp/form.html', context=templateDict)


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
