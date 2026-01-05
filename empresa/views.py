from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from empresa.models import Empresa, Vaga
import re


def index(request):
    return render(request, 'empresa/base_empresa.html')


@login_required(login_url='login')
def tela_principal_empresa(request):
    if request.user.tipo_usuario != 'empresa':
        return redirect('login')

    try:
        empresa = Empresa.objects.get(usuario=request.user)
    except Empresa.DoesNotExist:
        return redirect('login')

    vagas = Vaga.objects.filter(empresa=empresa)

    context = {

        'vagas_ativas': vagas.filter(ativa=True),
        'vagas_arquivadas': vagas.filter(ativa=False),

        'empregos_ativos':vagas.filter(tipo='emprego',ativa=True).order_by('-criada_em'),
        'estagios_arquivados': vagas.filter(tipo='emprego',ativa=False).order_by('-criada_em'),

        'estagios_ativos':vagas.filter(tipo='estagio',ativa=True),
        'estagio_arquivados':vagas.filter(tipo='estagio',ativa=False),

        'total_vagas': vagas.count(),
        'total_ativas': vagas.filter(ativa=True).count(),
        'total_arquivadas': vagas.filter(ativa=False).count(),
    }

    return render(request,'empresa/tela_principal_empresa.html',context)


@login_required(login_url='login')
def cadastrar_emprego(request):
    if request.user.tipo_usuario != 'empresa':
        return redirect('login')

    try:
        empresa = Empresa.objects.get(usuario=request.user)
    except Empresa.DoesNotExist:
        return redirect('login')

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        quantidade = request.POST.get('quantidade') or 1
        requisitos = request.POST.get('requisitos')
        modelo_trabalho = request.POST.get('modelo_trabalho')
        tipo_contrato = request.POST.get('tipo_contrato')
        jornada = request.POST.get('jornada')
        faixa_salarial = request.POST.get('faixa_salarial') or 0
        vale_refeicao = bool(request.POST.get('vale_refeicao'))
        plano_saude = bool(request.POST.get('plano_saude'))
        vale_transporte = bool(request.POST.get('vale_transporte'))
        outros_beneficios = bool(request.POST.get('outros_beneficios'))
        diferencial = request.POST.get('diferencial')
        descricao = request.POST.get('descricao')

        if not titulo or not requisitos or not modelo_trabalho or not tipo_contrato:
            messages.error(request, 'Preencha os campos obrigatórios.')
            return render(request, 'empresa/cadastrar_emprego.html')

        Vaga.objects.create(
            empresa=empresa,
            tipo='emprego',
            titulo=titulo,
            quantidade=quantidade,
            requisitos=requisitos,
            modelo_trabalho=modelo_trabalho,
            tipo_contrato=tipo_contrato,
            jornada=jornada,
            faixa_salarial=faixa_salarial,
            vale_refeicao=vale_refeicao,
            plano_saude=plano_saude,
            vale_transporte=vale_transporte,
            outros_beneficios=outros_beneficios,
            diferencial=diferencial,
            descricao=descricao
        )

        messages.success(request, 'Vaga cadastrada com sucesso.')
        return redirect('empresa:tela_principal_empresa')

    return render(request, 'empresa/cadastrar_emprego.html')

@login_required(login_url='login')
def detalhes_vaga(request, vaga_id):
    empresa = Empresa.objects.get(usuario=request.user)
    vaga = Vaga.objects.get(id=vaga_id,empresa=empresa)
    return render(request, 'empresa/detalhes_vaga.html',{'vaga':vaga})

@login_required(login_url='login')
def detalhes_estagio(request, vaga_id):
    empresa = Empresa.objects.get(usuario=request.user)
    vaga = Vaga.objects.get(id=vaga_id,empresa=empresa)
    return render(request, 'empresa/detalhes_estagio.html',{'vaga':vaga})


@login_required(login_url='login')
def cadastrar_estagio(request):
    if request.user.tipo_usuario != 'empresa':
        return redirect('login')
    
    try:
        empresa = Empresa.objects.get(usuario=request.user)
    except Empresa.DoesNotExist:
        return redirect('login')
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        quantidade = request.POST.get('quantidade') or 1
        requisitos = request.POST.get('requisitos')
        modelo_trabalho = request.POST.get('modelo_trabalho')
        tipo_contrato = request.POST.get("tipo_contrato")
        jornada = request.POST.get('jornada')
        faixa_salarial = request.POST.get('faixa_salarial') or 0
        vale_refeicao = bool(request.POST.get('vale_refeicao'))
        plano_saude = bool(request.POST.get('plano_saude'))
        vale_transporte = bool(request.POST.get('vale_transporte'))
        outros_beneficios = bool(request.POST.get('outros_beneficios'))
        diferencial = request.POST.get('diferencial')
        descricao = request.POST.get('descricao')

        if not titulo or not requisitos or not modelo_trabalho:
            messages.error(request,'Preencha os campos obrigatórios.')
            return render(request,'empresa/cadastrar_estagio.html')
        
        Vaga.objects.create(
            empresa=empresa,
            tipo='estagio',
            titulo=titulo,
            quantidade=quantidade,
            requisitos=requisitos,
            modelo_trabalho=modelo_trabalho,
            tipo_contrato=tipo_contrato,
            jornada=jornada,
            faixa_salarial=faixa_salarial,
            vale_refeicao=vale_refeicao,
            plano_saude=plano_saude,
            vale_transporte=vale_transporte,
            outros_beneficios=outros_beneficios,
            diferencial=diferencial,
            descricao=descricao 
        )

        messages.success(request,'Vaga de estágio cadastrada com suceesso.')
        return redirect('empresa:tela_principal_empresa')
    
    return render(request, 'empresa/cadastrar_estagio.html')


def perfil_empresa(request):
    return render(request, 'empresa/perfil_empresa.html')


def vagas_empresa(request):
    return render(request, 'empresa/vagas.html')


def lista_candidatos(request):
    return render(request, 'empresa/lista_candidatos.html')


def visualizar_curriculo(request):
    return render(request, 'empresa/visualizar_curriculo.html')

@login_required(login_url='login')
def editar_vaga(request,vaga_id):
    empresa = Empresa.objects.get(usuario=request.user)
    vaga = get_object_or_404(Vaga,id=vaga_id,empresa=empresa)

    if request.method == 'POST':
        vaga.titulo = request.POST.get('titulo')
        vaga.quantidade = request.POST.get('quantidade') or 1
        vaga.requisitos = request.POST.get('requisitos')
        vaga.modelo_trabalho = request.POST.get('modelo_trabalho')
        vaga.tipo_contrato = request.POST.get('tipo_contrato')
        vaga.jornada = request.POST.get('jornada')
        vaga.faixa_salarial = request.POST.get('faixa_salarial') or 0
        vaga.vale_refeicao = bool(request.POST.get('vale_refeicao'))
        vaga.plano_saude = bool(request.POST.get('plano_saude'))
        vaga.vale_transporte = bool(request.POST.get('vale_transporte'))
        vaga.outros_beneficios = bool(request.POST.get('outros_beneficios'))
        vaga.diferencial = request.POST.get('diferencial')
        vaga.descricao = request.POST.get('descricao')

        vaga.save()

        messages.success(request,'Vaga atualizada com sucesso.')
        return redirect('empresa:detalhes_vaga',vaga_id=vaga.id)
    
    return render(request, 'empresa/editar_vaga.html',{
        'vaga':vaga
    })


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
