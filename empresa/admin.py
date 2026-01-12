from django.contrib import admin
from .models import Empresa,Vaga,Candidatura

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'email')
    search_fields = ('razao_social', 'cnpj', 'email')

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'empresa',
        'modelo_trabalho',
        'tipo_contrato',
        'ativa',
        'criada_em'
    )
    list_filter = (
        'modelo_trabalho',
        'tipo_contrato',
        'ativa',
        'criada_em'
    )

    search_fields = (
        'titulo',
        'empresa__razao_social'
    )

    ordering = ('-criada_em',)
    list_per_page = 20

@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = (
        'vaga',
        'candidato',
        'data_inscricao'
    )