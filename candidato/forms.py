from django import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = [
            'nome', 'email', 'cpf', 'telefone', 'cidade',
            'foto_perfil', 'formacao', 'experiencia'
        ]
        widgets = {
            'formacao': forms.Textarea(attrs={'rows': 3}),
            'experiencia': forms.Textarea(attrs={'rows': 3}),
        }
