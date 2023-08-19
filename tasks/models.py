from django.db import models
from django.urls import path, include
from django.contrib.auth.models import User



# Create your models here.
class Tasks(models.Model):
    titulo = models.CharField(max_length=200)
    descripsion = models.TextField(max_length=200)
    tecnologia = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo