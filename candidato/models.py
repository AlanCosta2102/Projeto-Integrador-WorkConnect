from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Candidato(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11,unique=True,db_index=True)
    email = models.EmailField()

    

    def __str__(self):
        return self.nome