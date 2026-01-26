from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    path('tela_principal_empresa/', views.tela_principal_empresa, name='tela_principal_empresa'), 
    
    path('perfil/', views.perfil_empresa, name='perfil_empresa'),
        
    path('vagas/', views.vagas_empresa, name='vagas_empresa'),

    path('vaga/<int:vaga_id>/lista_candidatos/', views.lista_candidatos, name='lista_candidatos'),

    path('cadastrar_emprego/', views.cadastrar_emprego, name= 'cadastrar_emprego'),

    path('cadastrar_estagio/', views.cadastrar_estagio, name= 'cadastrar_estagio'),

    path('tela_principal_empresa/', views.tela_principal_empresa, name='tela_principal_empresa'),

    path('criar_conta_empresa/', views.criar_conta_empresa, name='criar_conta_empresa'),

    path('visualizar_curriculo/<int:id>/', views.visualizar_curriculo, name='visualizar_curriculo'),

    path('vaga/<int:vaga_id>/editar/', views.editar_vaga, name='editar_vaga'),

    path('perfil_empresa',views.perfil_empresa,name='perfil_empresa'),

    path('vaga/<int:vaga_id>/',views.detalhes_vaga,name='detalhes_vaga'),

    path('vaga/<int:vaga_id>/',views.detalhes_estagio,name='detalhes_estagio'),

    path('vaga/<int:vaga_id>/arquivar/',views.arquivar_vaga,name='arquivar_vaga'),
]