from django.db import models
from veiculo.consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS,default=1)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES,default=1)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEL,default=1)
    foto = models.ImageField(blank=True,null=True,upload_to='veiculos/fotos')


