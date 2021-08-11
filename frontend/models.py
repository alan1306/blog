from django.db import models
from django.db.models.base import Model

class User(models.Model):
    username=models.CharField(max_length=50,unique=True)
    