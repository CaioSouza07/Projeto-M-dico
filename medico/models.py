from django.db import models
from django.contrib.auth.models import User

def is_medico(user):
    return DadosMedico.objects.filter(user = user).exists()

# Create your models here.

class Especialidades(models.Model):
    especialidade = models.CharField(max_length = 100)

    def __str__(self):
        return self.especialidade

class DadosMedico(models.Model):

    crm = models.CharField(max_length = 30)
    nome = models.CharField(max_length=100)
    cep =  models.CharField(max_length=15)
    rua =  models.CharField(max_length=100)
    bairo =  models.CharField(max_length=100)
    numero = models.IntegerField()
    rg = models.ImageField(upload_to = 'rgs')
    cedulaIdentidadeMedica = models.ImageField(upload_to='cim')
    foto = models.ImageField(upload_to='fotos_perfil')
    descricao = models.TextField()
    valorConsulta = models.FloatField(default=100)
    user = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username