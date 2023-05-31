from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'exemplos/home.html')

def get_bootstrap(request):
    return render(request, 'exemplos/01_helow_word.html')
def get_bootstrap_containers(request):
    return render(request, 'exemplos/02_containers.html')

def get_bootstrap_grids(request):
    return render(request, 'exemplos/04_grids.html')

def get_bootstrap_grids2(request):
    return render(request, 'exemplos/05_grids.html')
def get_bootstrap_grids3(request):
    return render(request, 'exemplos/06_grids.html')
def get_bootstrap_layouts01(request):
    return render(request, 'exemplos/07_layouts.html')

def get_bootstrap_layouts02(request):
    return render(request, 'exemplos/08_layouts.html')

def get_bootstrap_layouts03(request):
    return render(request, 'exemplos/09_layouts.html')

def get_bootstrap_alin_hor(request):
    return render(request, 'exemplos/10_alinhamento.html')

def get_bootstrap_alin_ver(request):
    return render(request, 'exemplos/11_alinhamento.html')

def get_bootstrap_utilitarios(request):
    return render(request, 'exemplos/12_utilitarios.html')
def get_bootstrap_collapse(request):
    return render(request, 'exemplos/13_collapse.html')

def get_bootstrap_display_flex(request):
    return render(request, 'exemplos/14_display_flex.html')

def get_bootstrap_display_flexII(request):
    return render(request, 'exemplos/15_display_flexII.html')
