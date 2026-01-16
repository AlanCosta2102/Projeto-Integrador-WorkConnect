from django.shortcuts import render,redirect,get_object_or_404
from core.validators import validar_cpf, validar_cnpj
from django.contrib.auth import authenticate,login as auth_login,logout,logout
from .models import Usuario
from candidato.models import Candidato
from empresa.models import Empresa,Vaga
from django.contrib import messages
import re

def login(request):
    if request.method == 'POST':
        identificacao_raw = request.POST.get('identificacao')
        senha = request.POST.get('senha')

        if not identificacao_raw or not senha:
            messages.error(request, 'Preencha todos os campos.')
            return redirect('login')

        identificacao = re.sub(r'\D', '', identificacao_raw)
        user = None

        if len(identificacao) == 11:
            candidato = Candidato.objects.filter(cpf=identificacao).first()
            if not candidato:
                messages.error(request, 'CPF não cadastrado.')
                return redirect('login')

            user = authenticate(
                request,
                username=candidato.usuario.username,
                password=senha
            )

        elif len(identificacao) == 14:
            empresa = Empresa.objects.filter(cnpj=identificacao).first()
            if not empresa:
                messages.error(request, 'CNPJ não cadastrado.')
                return redirect('login')

            user = authenticate(
                request,
                username=empresa.usuario.username,
                password=senha
            )

        else:
            user = authenticate(
                request,
                username=identificacao_raw,
                password=senha
            )

        if not user:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')

        auth_login(request, user)

        if user.tipo_usuario == 'admin':
            return redirect('administrador:dashboard')

        if getattr(user, 'tipo_usuario', None) == 'empresa':
            return redirect('empresa:tela_principal_empresa')

        if getattr(user, 'tipo_usuario', None) == 'candidato':
            return redirect('candidato:tela_principal_candidato')

        messages.error(request, 'Tipo de usuário inválido.')
        return redirect('login')

    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def tela_selecao(request):
    return render(request,'core/tela_selecao.html')

def cadastro_candidato(request):
    if request.method == 'POST':
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']
        cpf_limpo = re.sub(r'\D','',request.POST['cpf'])

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem')
            return redirect('candidato:criar_conta')
        
        if not validar_cpf(cpf_limpo):
            messages.error(request,'CPF inválido.')
            return redirect('candidato:criar_conta')
        
        if Candidato.objects.filter(cpf=cpf_limpo).exists():
            messages.error(request,'CPF já cadastrado.')
            return redirect('candidato:criar_conta')

        user = Usuario.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=senha,
            tipo_usuario = 'candidato'
        )

        user.tipo_usuario = 'candidato'
        user.save()

        Candidato.objects.create(
            usuario=user,
            nome=request.POST['nome'],
            cpf=cpf_limpo,
            email=request.POST['email']
        )

        auth_login(request, user)
        return redirect('candidato:tela_principal_candidato')

    return render(request, 'candidato/criar_conta.html')


def cadastro_empresa(request):
    if request.method == 'POST':
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']
        cnpj_limpo = re.sub(r'\D','',request.POST['cnpj'])

        if senha != confirmar:
            messages.error(request,'As senhas não são iguais.')
            return redirect('criar_conta_empresa')
        
        if not validar_cnpj(cnpj_limpo):
            messages.error(request,'CNPJ inválido.')
            return redirect('criar_conta_empresa')
        
        if Empresa.objects.filter(cnpj=cnpj_limpo).exists():
            messages.error(request,'CNPJ já cadastrado.')
            return redirect('criar_conta_empresa')


        user = Usuario.objects.create_user(
            username=cnpj_limpo,  
            email=request.POST['email'],
            password=senha,
            tipo_usuario='empresa'
        )

        Empresa.objects.create(
            usuario=user,
            razao_social=request.POST['nome_empresa'],
            cnpj=cnpj_limpo, 
            email=request.POST['email']
        )

        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login')

    return render(request,'empresa/criar_conta_empresa.html')


