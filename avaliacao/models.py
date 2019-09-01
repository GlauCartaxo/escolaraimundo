from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Avaliacao(models.Model):
    professor = models.ForeignKey("users.User", verbose_name=("professor"),
    related_name='AvaliacaoProAluno',  on_delete=models.CASCADE)
    aluno = models.ForeignKey("users.User", verbose_name=("aluno"), on_delete=models.CASCADE)
    nota = models.CharField(max_length=4)

    def str(self):
        return f'Avaliacao {self.pk} | Professor {self.professor}' 