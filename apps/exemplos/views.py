from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from . import form_exemplo
import re

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
def get_bootstrap_formulario_I(request):
    return render(request,'exemplos/16_forms_parte_i.html')

def get_bootstrap_processa_formulario_v1(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    isEmail, isSenha = validou_form(email, senha)
    if isEmail and isSenha:
        return HttpResponseRedirect("/")
    else:
        context = {
            'email_st': 'is-valid' if isEmail else 'is-invalid',
            'senha_st': 'is-valid' if isSenha else 'is-invalid',
            'email': email,
            'senha': senha,
        }

        return render(request, 'exemplos/16_forms_parte_i.html', context)

def validou_senha(senha):
    regex = '^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{6,15}$'
    if (re.search(regex, senha)):
        return True
    else:
        return False

def validou_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        return True
    else:
        return False
def validou_form(email, senha):
    isEmail = validou_email(email)
    isSenha = validou_senha(senha)
    return isEmail, isSenha

def get_bootstrap_formulario_II(request):
    form = form_exemplo.FormExemplo()

    context ={
        'form': form
    }
    return render(request,'exemplos/17_forms_parte_ii.html', context)

def get_bootstrap_processa_formulario_v2(request):
    form = form_exemplo.FormExemplo()

    if request.method == 'POST':
        form = form_exemplo.FormExemplo(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            mensagem = form.cleaned_data['mensagem']
            mensagem_html = f'Formulário validado com sucesso.<br>Email: {email}' \
                            f'<br>Senha: {senha}<br>Mensagem: {mensagem}'
            return HttpResponse(mensagem_html)
        else:
            print("Deu Ruim!!!")


        return render(request, 'exemplos/17_forms_parte_ii.html', {'form': form})
