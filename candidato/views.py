from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from candidato.models import Candidato
from empresa.models import Vaga
from django.contrib import messages
import re

def index(request):
    return render(request, 'candidato/base.html')

@login_required(login_url='login')
def tela_principal_candidato(request):
    if request.user.tipo_usuario != 'candidato':
        return redirect('login')
    
    ultimas_vagas = (
        Vaga.objects.filter(ativa=True)
        .order_by('-criada_em')[:9]
    )
    return render(request, 'candidato/tela_principal_candidato.html',{
        'ultimas_vagas':ultimas_vagas
    })


def candidaturas_candidato(request):
    return render(request, 'candidato/candidaturas.html')

@login_required(login_url='login')
def vagas_candidato(request):
    vagas =Vaga.objects.filter(ativa=True).order_by('-criada_em')

    return render(request, 'candidato/vagas.html',{
         'vagas':vagas
    })

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

def perfil_candidato(request):
    return render(request, 'candidato/perfil_candidato.html')

def perfil_empresa(request):
    return render(request, 'candidato/perfil_empresa.html')

@login_required
def inscricao(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id, ativa=True)

    if request.method == 'POST':

     return redirect('candidato:inscricao', vaga_id=vaga.id)
    
    return render(request,'candidato/inscricao.html')

def detalhes_vaga(request,vaga_id):
    vaga = get_object_or_404(Vaga,id=vaga_id,ativa=True)

    return render(request,'candidato/detalhes_vaga.html',{
        'vaga':vaga
    })
