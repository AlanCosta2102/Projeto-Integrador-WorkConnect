from django.shortcuts import render

def dashboard(request):
    return render(request, 'administrador/dashboard.html')

def gerenciamento_view(request):
    return render(request, 'administrador/gerenciamento.html')

def tela_moderar_vagas_view(request):
    return render(request,'administrador/tela_moderar_vagas.html')
    
