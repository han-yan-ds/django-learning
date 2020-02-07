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