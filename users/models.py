from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True) #unique para ser usado em rg e cpf pois só existe 1 de cada por pessoa
    nome = models.CharField('Nome', max_length = 100)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)    
    rg = models.CharField('RG', max_length = 13, unique=True)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    

