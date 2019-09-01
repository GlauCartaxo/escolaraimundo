from django.db import models
from users.models import Usuario
# Create your models here.

class Avaliacao(models.Model):
    professor = models.ForeignKey("users.Usuario", verbose_name=("professor"),
    related_name='AvaliacaoProAluno',  on_delete=models.CASCADE)
    aluno = models.ForeignKey("users.Usuario", verbose_name=("aluno"), on_delete=models.CASCADE)
    nota = models.CharField('nota', max_length=5)

    def str(self):
        return f'Avaliacao {self.pk} | Professor {self.professor}' 