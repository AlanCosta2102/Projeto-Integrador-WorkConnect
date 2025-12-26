from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from candidato.models import Candidato
from django.contrib import messages
import re

def index(request):
    return render(request, 'candidato/base.html')

@login_required(login_url='login')
def tela_principal_candidato(request):
    return render(request, 'candidato/tela_principal_candidato.html')

# def perfil_candidato(request):
#     return render(request, 'candidato/perfil.html') 

def candidaturas_candidato(request):
    return render(request, 'candidato/candidaturas.html')

def vagas_candidato(request):
    return render(request, 'candidato/vagas.html')

def criar_conta(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar')

        if not all([nome, cpf, email, senha, confirmar]):
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'candidato/criar_conta.html')

        if senha != confirmar:
            messages.error(request, 'As senhas não conferem.')
            return render(request, 'candidato/criar_conta.html')

        cpf_limpo = re.sub(r'\D', '', cpf)

        if Candidato.objects.filter(cpf=cpf_limpo).exists():
            messages.error(request, 'CPF já cadastrado.')
            return render(request, 'candidato/criar_conta.html')

        usuario = Usuario.objects.create_user(
            username=cpf_limpo,
            email=email,
            password=senha,
            tipo_usuario='candidato'
        )

        Candidato.objects.create(
            usuario=usuario,
            nome=nome,
            cpf=cpf_limpo,
            email=email
        )

        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login')  

    return render(request, 'candidato/criar_conta.html')

def descricao_vaga(request):
    return render(request, 'candidato/descricao_vaga.html')

def perfil_candidato(request):
    return render(request, 'candidato/perfil_candidato.html')

def perfil_empresa(request):
    return render(request, 'candidato/perfil_empresa.html')

def inscricao(request):
    return render(request,'candidato/inscricao.html')