"""
It may feel weird that these classes have no constructor (no __init__ function).  For good REASON. 

An object is created by calling ClassName(field1=value, field2=value, ....),
AND, the SQL INSERT command isn't complete until .save() is called

Eg:
>>> from SecondApp.models import Topic
>>> t = Topic(topic_name="Sports")
>>> t.save()
"""


from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=64, unique=True)
    
    def ___repr__(self):
        return self.topic_name
    
    def __str__(self):
        return self.___repr__()


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    url = models.URLField(unique=True)


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __repr__(self):
        return str(self.date)


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=64)
    email = models.EmailField()