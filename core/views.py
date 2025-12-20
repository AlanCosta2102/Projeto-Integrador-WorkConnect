from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Usuario
from candidato.models import Candidato
from empresa.models import Empresa
from django.contrib import messages

def login(request):
    return render(request, 'core/login.html')

def tela_selecao(request):
    return render(request,'core/tela_selecao.html')

def cadastro_candidato(request):
    if request.method == 'POST':
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem')
            return redirect('criar_conta')

        user = Usuario.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=senha,
            tipo_usuario='candidato'
        )

        Candidato.objects.create(
            usuario=user,
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            email=request.POST['email']
        )

        return redirect('login')

    return render(request, 'candidato/criar_conta.html')

def cadastro_empresa(request):
    if request.method == 'POST':
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']

        if senha != confirmar:
            messages.error(request,'As senhas não são iguais.')
            return redirect('criar_conta_empresa')
        
        user = Usuario.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=senha,
            tipo_usuario='empresa'
        )

        Empresa.objects.create(
            usuario=user,
            razao_social=request.POST['nome_empresa'],
            cnpj=request.POST['cnpj'],
            email=request.POST['email']
        )

        return redirect('login')
    
    return render(request,'empresa/criar_conta_empresa.html')