from django.shortcuts import render,redirect
from core.models import Usuario
from empresa.models import Empresa
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re

def index(request):
    return render(request, 'empresa/base_empresa.html')

@login_required(login_url='login')
def tela_principal_empresa(request):
    return render(request, 'empresa/tela_principal_empresa.html')

def perfil_empresa(request):
    return render(request, 'empresa/perfil.html') 

def cadastrar_vagas(request):
    return render(request, 'empresa/cadastrar_vagas.html')

def vagas_empresa(request):
    return render(request, 'empresa/vagas.html')

def lista_candidatos(request):
    return render(request,'empresa/lista_candidatos.html')

def cadastrar_emprego(request):
    return render(request, 'empresa/cadastrar_emprego.html')

def cadastrar_estagio(request):
    return render(request, 'empresa/cadastrar_estagio.html')

def tela_principal_empresa(request):
    return render(request, 'empresa/tela_principal_empresa.html')

def criar_conta_empresa(request):
    if request.method == 'POST':
        razao_social = request.POST.get('nome_empresa')
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar')

        if not all([razao_social, cnpj, email, senha, confirmar]):
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'empresa/criar_conta_empresa.html')

        if senha != confirmar:
            messages.error(request, 'As senhas não conferem.')
            return render(request, 'empresa/criar_conta_empresa.html')

        cnpj_limpo = re.sub(r'\D', '', cnpj)

        if Empresa.objects.filter(cnpj=cnpj_limpo).exists():
            messages.error(request, 'CNPJ já cadastrado.')
            return render(request, 'empresa/criar_conta_empresa.html')

        usuario = Usuario.objects.create_user(
            username=cnpj_limpo,
            email=email,
            password=senha,
            tipo_usuario='empresa'
        )

        Empresa.objects.create(
            usuario=usuario,
            razao_social=razao_social,
            cnpj=cnpj_limpo,
            email=email
        )

        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login')  
    return render(request, 'empresa/criar_conta_empresa.html')

def visualizar_curriculo(request):
    return render(request, 'empresa/visualizar_curriculo.html')

def editar_vaga(request):
    return render(request, 'empresa/editar_vaga.html')

def perfil_empresa(request):
    return render(request,'empresa/perfil_empresa.html')

