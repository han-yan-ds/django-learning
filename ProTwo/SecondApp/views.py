from django.shortcuts import render
from django.http import HttpResponse
from SecondApp.models import Topic, Webpage, AccessRecord, User
from SecondApp.forms import UserForm
# Create your views here.

def index(req):
    return render(req, 'SecondApp/index.html', context={})


def imageDemo(req):
    templateDict = {
        'template_exercise':  "Demo-ing Image",
    }
    return render(req, 'SecondApp/imageDemo.html', context=templateDict)


def users(req):
    userList = User.objects.order_by('lname')
    userDict = {'users': userList}
    return render(req, 'SecondApp/users.html', context=userDict)


def userFormPage(req):
    formInstance = UserForm()
    templateDict = {
        'form': formInstance
    }
    if req.method == "POST":
        formInstance = UserForm(req.POST)
        if formInstance.is_valid():
            # do stuff with form data
            formInstance.save(commit=True)
            return users(req) # return to users list
    return render(req, 'SecondApp/userForm.html', context=templateDict)

