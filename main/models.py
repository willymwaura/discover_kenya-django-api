from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Feature (models.Model):
    
    task=models.CharField(max_length=1000)
    email=models.EmailField(default='user@gmail.com')
    

    def __string__(self):
        return self.task   


