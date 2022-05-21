from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=12)
    REQUIRED_FIELD=['username','phone','first_name','last_name']
    def get_username(self):
        return self.email