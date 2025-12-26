from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('login')
    
    return render(request, 'administrador/dashboard.html')

def gerenciamento_view(request):
    return render(request, 'administrador/gerenciamento.html')

def tela_moderar_vagas_view(request):
    return render(request,'administrador/tela_moderar_vagas.html')
    
