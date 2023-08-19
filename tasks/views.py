from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Tasks


# from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {
        'form': UserCreationForm
    })


def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                auth_login(request, user)
                return redirect(acceso)

            except:
                return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    "error": 'Ha ocurrido un error al crear el usuario'
                })
        else:
            return render(request, 'registrarse.html', {
                "form": UserCreationForm,
                "error": 'Las contraseñas no coinciden'
            })


def acceso(request):
    if request.method == 'GET':
        return render(request, 'acceso.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'acceso.html', {
                'form': AuthenticationForm,
                'error': 'usuario o contraseña incorrecto'
            })
        else:
            auth_login(request,user)
            return redirect('home')


def cerrar_sesion(request):
    logout(request)
    return redirect('acceso')

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()        