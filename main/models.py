from django.db import models
from datetime import datetime

from pytz import timezone

# Create your models here.

class Feature(models.Model):
    region=models.CharField(max_length=100,default='Central')
    title=models.CharField(max_length=100,default='Tsavo')
    image_url=models.URLField(max_length=30,default="//cdn.weatherapi.com/weather/64x64/day/116.png")
    experience=models.CharField(max_length=100,default='i loved it')
    created=models.DateTimeField(auto_now_add=True,blank=True)
    nearby_town=models.CharField(max_length=100,default="nairobi")
    weather_text=models.CharField(max_length=100,default="warm",blank=True)
    degree_celcius=models.IntegerField(default=20,blank=True)
    weather_url=models.URLField(max_length=30,blank=True)
    def __str__(self):
        return '{}{}'.format(self.region,self.title)