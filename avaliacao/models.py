from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Avaliacao(models.Model):
    professor = models.ForeignKey("users.User", verbose_name=("professor"),
    related_name='AvaliacaoProAluno',  on_delete=models.CASCADE)
    aluno = models.ForeignKey("users.User", verbose_name=("aluno"), on_delete=models.CASCADE)
<<<<<<< HEAD
    nota = models.CharField('nota', max_length=5)
=======
    nota = models.CharField(max_length=4)
>>>>>>> 214dc7d4fb3eccecce70c0b1a732ed1c4e346863

    def str(self):
        return f'Avaliacao {self.pk} | Professor {self.professor}' 