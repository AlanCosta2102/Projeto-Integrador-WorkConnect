# administrador/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('gerenciamento/', views.gerenciamento_view, name='gerenciamento'),
    path('tela_moderar_vagas/',views.tela_moderar_vagas_view,name='tela_moderar_vagas'),
]
