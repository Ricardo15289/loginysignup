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


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
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
                return redirect(login)

            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'An error occurred while creating the user.'
                })
        else:
            return render(request, 'signup.html', {
                "form": UserCreationForm,
                "error": 'The passwords do not match'
            })


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Invalid username or password'
            })
        else:
            auth_login(request,user)
            return redirect('home')


def sign_out(request):
    logout(request)
    return redirect('login')

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()     