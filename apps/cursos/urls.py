from django.urls import path, include
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos, name='cursos'),

]