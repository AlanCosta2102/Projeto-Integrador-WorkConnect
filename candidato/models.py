from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Candidato(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True, db_index=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='candidatos/', blank=True, null=True)

    formacao = models.TextField(blank=True, null=True)

    experiencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
