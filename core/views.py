from django.shortcuts import render

def login(request):
    return render(request, 'core/login.html')

def tela_selecao(request):
    return render(request,'core/tela_selecao.html')