from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('tela_selecao/',views.tela_selecao,name='tela_selecao'),
]
