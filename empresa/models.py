from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Empresa(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()

    