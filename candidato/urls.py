from django.urls import path
from . import views

app_name = 'candidato'

urlpatterns = [
    path('tela_principal_candidato/', views.tela_principal_candidato, name='tela_principal_candidato'), 
    
    # path('perfil/', views.perfil_candidato, name='perfil_candidato'),
    
    path('candidaturas/', views.candidaturas_candidato, name='candidaturas_candidato'),
    
    path('vagas/', views.vagas_candidato, name='vagas_candidato'),

    path('criar_conta/', views.criar_conta, name='criar_conta'),   

    path('descricao_vaga/', views.descricao_vaga, name= 'descricao_vaga'),

    path('perfil_candidato/', views.perfil_candidato, name='perfil_candidato'),

     path('perfil_empresa/', views.perfil_empresa, name='perfil_empresa'),

     path('inscricao/',views.inscricao,name='inscricao'),

]