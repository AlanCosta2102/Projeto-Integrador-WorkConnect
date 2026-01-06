from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    TIPOS = (
        ('candidato','Candidato'),
        ('empresa','Empresa'),
        ('admin','Administrador'),
    )

    tipo_usuario = models.CharField(max_length=10,choices=TIPOS,default='admin')