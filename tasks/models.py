from django.db import models
from django.urls import path, include
from django.contrib.auth.models import User



# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    technology = models.CharField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title