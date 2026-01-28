# administrador/urls.py
from django.urls import path
from . import views

app_name = 'administrador'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('gerenciamento/', views.gerenciamento_view, name='gerenciamento'),
    path('tela_moderar_vagas/',views.tela_moderar_vagas_view,name='tela_moderar_vagas'),
    path('excluir-usuario/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    path('detalhes-usuario/<int:id>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('excluir-vaga/<int:vaga_id>/', views.excluir_vaga,name='excluir_vaga'),
]
