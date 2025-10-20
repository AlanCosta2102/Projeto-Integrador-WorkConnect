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