from django.db import models
from datetime import datetime

from pytz import timezone

# Create your models here.

class Feature(models.Model):
    region=models.CharField(max_length=100,default='Central')
    title=models.CharField(max_length=100,default='Tsavo')
    experience=models.CharField(max_length=100,default='i love it')
    created=models.DateTimeField(auto_now_add=True,blank=True)
    nearby_town=models.CharField(max_length=100,default="nairobi")
    weather=models.CharField(max_length=100,default="nairobi")
    def __str__(self):
        return '{}{}'.format(self.region,self.title)