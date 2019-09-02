from django.db import models
from users.models import Usuario
# Create your models here.

class Avaliacao(models.Model):
    professor = models.ForeignKey("users.Professor", verbose_name=("nota_professor"),
    related_name='avaliacaoFromProfessor',  on_delete=models.CASCADE)
    aluno = models.ForeignKey("users.Aluno", verbose_name=("nota_aluno"),related_name='avaliacaoFromAluno', on_delete=models.CASCADE)
    nota = models.CharField('nota', max_length=5)
    realisacao = models.DateTimeField(auto_now_add=False)

    def str(self):
        return f'Avaliacao {self.pk} | Realisacao {self.realisacao} | Professor {self.professor} | Aluno {self.aluno}' 
    
    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'