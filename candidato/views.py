from django.shortcuts import render

def index(request):
    return render(request, 'candidato/base.html')

def tela_principal_candidato(request):
    return render(request, 'candidato/tela_principal_candidato.html')

def perfil_candidato(request):
    return render(request, 'candidato/perfil.html') 

def candidaturas_candidato(request):
    return render(request, 'candidato/candidaturas.html')

def vagas_candidato(request):
    return render(request, 'candidato/vagas.html')

def criar_conta(request):
    return render(request, 'candidato/criar_conta.html')

def descricao_vaga(request):
    return render(request, 'candidato/descricao_vaga.html')

def perfil_candidato(request):
    return render(request, 'candidato/perfil_candidato.html')

def perfil_empresa(request):
    return render(request, 'candidato/perfil_empresa.html')