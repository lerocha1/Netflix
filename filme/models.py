"""AQui no models é onde o python conversa, cria e armazena informações no BD"""

from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Ánalises"),
    ("PROGRAMACAO", "Programacao"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

LISTA_SEXO = (
    ("MASCULIO",'Masculino'),
    ("FEMININO","Feminino"),
)
#criar filme
class Filme(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes')
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(max_length=1000)
    categoria =models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criação = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.titulo

#criar episodios
class Seriado(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes')
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(max_length=1000)
    categoria =models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criação = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.titulo

#criar usuario
class Usuario(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=20, unique=True)
    sexo = models.CharField(max_length=8, choices=LISTA_SEXO)

    def __str__(self):
        return self.usuario



