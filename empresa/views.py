from django.shortcuts import render

def index(request):
    return render(request, 'empresa/base_empresa.html')

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
    return render(request, 'empresa/criar_conta_empresa.html')