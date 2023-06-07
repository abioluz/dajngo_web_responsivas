from django.urls import path, include
from . import views

app_name = 'contato'

urlpatterns = [
    path('', views.contato, name='contato'),
    path('mensagens', views.processa_contato, name='mensagens'),

]
