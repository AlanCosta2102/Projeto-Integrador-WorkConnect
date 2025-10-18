from django.shortcuts import render

def index(request):
    return render(request, 'empresa/index.html')
