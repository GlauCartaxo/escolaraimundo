from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'cpf', 'nome','dtNascimento', 'rg' ]
   