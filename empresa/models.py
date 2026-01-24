from django.db import models
from core.models import Usuario
from django.conf import settings
from django.contrib.auth.models import User


User = settings.AUTH_USER_MODEL

class Empresa(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14,unique=True,db_index=True)
    email = models.EmailField()

    telefone = models.CharField(max_length=20,blank=True,null=True)
    instagram = models.CharField(max_length=100,blank=True,null=True)

    estado = models.CharField(max_length=50,blank=True,null=True)
    cidade = models.CharField(max_length=50,blank=True,null=True)
    bairro = models.CharField(max_length=100,blank=True,null=True)
    complemento = models.CharField(max_length=255,blank=True,null=True)

    sobre = models.TextField(blank=True,null=True)

    foto_perfil = models.ImageField(upload_to='empresas/perfil/',blank=True,null=True)
    capa = models.ImageField(upload_to='empresas/perfil/',blank=True,null=True)

    def __str__(self):
        return self.razao_social

class Vaga(models.Model):
    TIPO_VAGA = [
        ('emprego','Emprego'),
        ('estagio','Estágio'),
    ]
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='vagas'
    )
    tipo = models.CharField(max_length=10, choices=TIPO_VAGA, default='emprego')

    titulo = models.CharField(max_length=100)
    quantidade = models.PositiveBigIntegerField(default=1)
  

    requisitos = models.TextField()

    MODELO_TRABALHO = [
        ('presencial','Presencial'),
        ('remoto','Remoto'),
        ('hibrido','Híbrido'),
    ]

    modelo_trabalho = models.CharField(max_length=20,choices=MODELO_TRABALHO)

    TIPO_CONTRATO = [
        ('clt','CLT'),
        ('pj','PJ'),
        ('temporario','Temporário'),
    ]

    tipo_contrato = models.CharField(max_length=20,choices=TIPO_CONTRATO)

    jornada = models.CharField(max_length=50)
    faixa_salarial = models.DecimalField(max_digits=10,decimal_places=2)

    vale_refeicao = models.BooleanField(default=False)
    plano_saude = models.BooleanField(default=False)
    vale_transporte = models.BooleanField(default=False)
    outros_beneficios = models.BooleanField(default=False)

    diferencial = models.CharField(max_length=255,blank=True,null=True)
    descricao = models.TextField()

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_VAGA
    )

    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.titulo}"
    
from candidato.models import Candidato

class Candidatura(models.Model):
    vaga = models.ForeignKey(
        'Vaga',
        on_delete=models.CASCADE,
        related_name='candidaturas'
    )
    candidato = models.ForeignKey(
        Candidato,
        on_delete=models.CASCADE,
        related_name='candidaturas'
    )
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidato.nome} - {self.vaga.titulo}"
