from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Funcionario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_funcionario = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=(('M', 'Masculino'), ('F', 'Feminino')))
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    pais = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    data_admissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    status_emprego = models.CharField(max_length=20, choices=(('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Temporário', 'Temporário')))
    foto_perfil = models.ImageField(upload_to='perfil_pics/', null=True, blank=True)  # Verifique se este campo está aqui



    def __str__(self):
        return f"{self.nome} {self.sobrenome}"