from django import forms
from avaliacao.models import Avaliacao

class AvaliacaoCreateForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota','realisacao', 'professor', 'aluno', ]  
      
    