from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    path('tela_principal_empresa/', views.tela_principal_empresa, name='tela_principal_empresa'), 
    
    path('perfil/', views.perfil_empresa, name='perfil_empresa'),
    
    path('cadastrar_vagas/', views.cadastrar_vagas, name='cadastrar_vagas'),
    
    path('vagas/', views.vagas_empresa, name='vagas_empresa'),

    path('lista_candidatos/', views.lista_candidatos, name='lista_candidatos')
]