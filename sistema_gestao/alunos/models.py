from django.db import models
from django.utils import timezone

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length = 255)
    data_nascimento = models.DateField()
    genero = models.CharField()
    numero = models.IntegerField()
    classe = models.IntegerField()
    sala = models.CharField()
    turno = models.CharField( default='Indefinido')
    curso = models.CharField(max_length=50) 
    ingresso = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nome