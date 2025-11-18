from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('tela_selecao/',views.tela_selecao,name='tela_selecao'),
]
