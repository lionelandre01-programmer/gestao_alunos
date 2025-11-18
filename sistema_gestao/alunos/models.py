from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Cursos(models.Model):
    nome = models.CharField(max_length=80)
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.nome
    

class Salas(models.Model):
    numero_sala = models.IntegerField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nome', 'email']

    def __str__(self):
        return self.nome
    
class Movimentos(models.Model):
    tipo = models.CharField(max_length=50)
    Aluno = models.CharField(max_length=50)
    funcionario = models.CharField(max_length=50)
    data_movimento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipo


class Alunos(models.Model):

    Sexos = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    Classes = [
        (10, '10ª Classe'),
        (11, '11ª Classe'),
        (12, '12ª Classe'),
        (13, '13ª Classe')
    ]

    Turnos = [
        ('Manhã', 'Turno da manhã'),
        ('Tarde', 'Turno da tarde'),
    ]

    Turmas = [
        ('A', 'Turma A'),
        ('B', 'Turma B'),
        ('C', 'Turma C'),
        ('D', 'Turma D'),
    ]

    nome = models.CharField(max_length = 255)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=5, choices=Sexos)
    tell = models.IntegerField()
    classe = models.IntegerField(choices=Classes)
    sala = models.ForeignKey('Salas', on_delete=models.SET_NULL, null=True, default=None)
    turno = models.CharField(max_length=10, choices=Turnos)
    curso = models.ForeignKey('Cursos', on_delete=models.SET_NULL, null=True, default=None)
    turma = models.CharField(max_length=5, choices=Turmas) 
    matricula = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nome
    
class Propinas(models.Model):
    aluno = models.ForeignKey('Alunos', on_delete=models.SET_NULL, null = True)
    mes = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.mes


class Mensalidade(models.Model):
    curso = models.ForeignKey('Cursos', on_delete=models.SET_NULL, null=True, default=None)
    classe10 = models.DecimalField(max_digits=10, decimal_places=2)
    classe11 = models.DecimalField(max_digits=10, decimal_places=2)
    classe12 = models.DecimalField(max_digits=10, decimal_places=2)
    classe13 = models.DecimalField(max_digits=10, decimal_places=2)

