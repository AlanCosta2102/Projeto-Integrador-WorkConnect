from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from candidato.models import Candidato
from empresa.models import Vaga, Empresa
from empresa.models import Candidatura
from django.contrib import messages
import re

def index(request):
    return render(request, 'candidato/base.html')

@login_required(login_url='login')
def tela_principal_candidato(request):
    if request.user.tipo_usuario != 'candidato':
        return redirect('login')

    candidato = Candidato.objects.get(usuario=request.user)

    
    total_vagas = Vaga.objects.filter(ativa=True).count()

    total_candidaturas = Candidatura.objects.filter(
        candidato=candidato
    ).count()

    total_empresas = Empresa.objects.count()

    
    ultimas_vagas = (
        Vaga.objects.filter(ativa=True)
        .order_by('-criada_em')[:9]
    )

    return render(request, 'candidato/tela_principal_candidato.html', {
        'ultimas_vagas': ultimas_vagas,
        'total_vagas': total_vagas,
        'total_candidaturas': total_candidaturas,
        'total_empresas': total_empresas,
    })

def candidaturas_candidato(request):
    candidato = get_object_or_404(
        Candidato,
        usuario=request.user
    )

    candidaturas = Candidatura.objects.filter(
        candidato=candidato
    ).select_related('vaga', 'vaga__empresa')

    return render(
        request,
        'candidato/candidaturas.html',
        {'candidaturas': candidaturas}
    )
@login_required(login_url='login')
def vagas_candidato(request):
    vagas = Vaga.objects.filter(ativa=True)

    titulo = request.GET.get('titulo')
    empresa = request.GET.get('empresa')
    cidade = request.GET.get('cidade')

    if titulo:
        vagas = vagas.filter(titulo__icontains=titulo)

    if empresa:
        vagas = vagas.filter(empresa__razao_social__icontains=empresa)

    if cidade:
        vagas = vagas.filter(empresa__cidade__icontains=cidade)

    vagas = vagas.order_by('-criada_em')

    return render(request, 'candidato/vagas.html', {
        'vagas': vagas
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

@login_required(login_url='login')
def perfil_candidato(request):
    return render(request, 'candidato/perfil_candidato.html')

@login_required(login_url='login')
def perfil_empresa(request):
    return render(request, 'candidato/perfil_empresa.html')

@login_required(login_url='login')
def inscricao(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id, ativa=True)

    candidato = get_object_or_404(
        Candidato,
        usuario=request.user
    )

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        curriculo = request.FILES.get('curriculo')

       
        if not all([nome, email, cpf]):
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'candidato/inscricao.html', {'vaga': vaga})

        cpf_limpo = re.sub(r'\D', '', cpf)

      
        candidato.nome = nome
        candidato.email = email
        candidato.cpf = cpf_limpo
        candidato.save()

        
        Candidatura.objects.get_or_create(
            candidato=candidato,
            vaga=vaga
        )

        messages.success(request, 'Candidatura realizada com sucesso!')
        return redirect('candidato:candidaturas_candidato')

    return render(request, 'candidato/inscricao.html', {'vaga': vaga})

def detalhes_vaga(request,vaga_id):
    vaga = get_object_or_404(Vaga,id=vaga_id,ativa=True)

    return render(request,'candidato/detalhes_vaga.html',{
        'vaga':vaga
    })
