from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'cpf', 'nome','dtNascimento', 'rg' ]
   