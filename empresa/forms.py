from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'foto_perfil',
            'razao_social',
            'telefone',
            'instagram',
            'estado',
            'cidade',
            'bairro',
            'complemento',
            'sobre',  
        ]

        widgets = {
            'razao_social':forms.TextInput(attrs={'class':'input'}),
            'telefone':forms.TextInput(attrs={'class':'input'}),
            'instagram':forms.TextInput(attrs={'class':'input'}),
            'estado':forms.TextInput(attrs={'class':'input'}),
            'cidade':forms.TextInput(attrs={'class':'input'}),
            'bairro':forms.TextInput(attrs={'class':'input'}),
            'complemento':forms.TextInput(attrs={'class':'input'}),
            'sobre':forms.Textarea(attrs={
                'class':'textarea',
                'rows':4
            }),
        }