from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class EscolaUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
# Create your models here.



class Usuario(AbstractBaseUser):
    """Model definition for Usuario."""

    nome = models.CharField(unique=True, max_length=30, verbose_name='nome')
    email = models.EmailField(unique=True)

    is_admin = models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    objects = EscolaUserManager()

    USERNAME_FIELD = 'email'    #Usado para logar, juntamente, com a senha

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    def __str__(self):
        return self.email


    @property
    def is_staff(self):
        return self.is_admin
        #aqui estamos conferindo se o usuário é admin

class Aluno(Usuario):
    rg = models.CharField(max_length=7, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    matricula = models.CharField(max_length=13, unique=True)
    def save(self, *args, **kwargs):
        self.is_aluno = True
        super(Aluno, self).save(*args, **kwargs)

# ////////////////////////////////////////////////////////////

class Professor(Usuario):
    IDProfessor = models.CharField(max_length=13, unique=True)

    def save(self, *args, **kwargs):
        self.is_professor = True
        super(Professor, self).save(*args, **kwargs)
    class Meta:
        permissions = (
            ('pode_mudar_nota', 'Pode mudar nota'),
        )
