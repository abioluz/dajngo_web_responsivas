from django.urls import path, include
from . import views

app_name = 'exemplos'

urlpatterns = [
    path('', views.home, name='home'),
    path('inicio', views.get_bootstrap, name='inicio'),
    path('containers', views.get_bootstrap_containers, name='containers'),
    path('grids', views.get_bootstrap_grids, name='grids'),
    path('grids2', views.get_bootstrap_grids2, name='grids2'),
    path('grids3', views.get_bootstrap_grids3, name='grids3'),
    path('layouts01', views.get_bootstrap_layouts01, name='layouts01'),
    path('layouts02', views.get_bootstrap_layouts02, name='layouts02'),
    path('layouts03', views.get_bootstrap_layouts03, name='layouts03'),
    path('alin_hor', views.get_bootstrap_alin_hor, name='alin_hor'),
    path('alin_ver', views.get_bootstrap_alin_ver, name='alin_ver'),
    path('utilitarios', views.get_bootstrap_utilitarios, name='utilitarios'),
    path('collapse', views.get_bootstrap_collapse, name='collapse'),
    path('display_flex', views.get_bootstrap_display_flex, name='display_flex'),
    path('display_flexii', views.get_bootstrap_display_flexII, name='display_flexii'),

]

