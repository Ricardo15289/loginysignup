from django.urls import path,include
#from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import TaskView
from tasks import views

router = DefaultRouter()
router.register(r'tasks', views.TaskView,)

urlpatterns = [
   path('api/v1/', include(router.urls)),
]

#genera todas las rutas GET,POST,PUT,DELETE