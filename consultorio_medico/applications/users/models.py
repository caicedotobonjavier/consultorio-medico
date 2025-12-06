from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
#
from model_utils.models import TimeStampedModel
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('ESP', 'Especialista'),
        ('MEDICO', 'Medico'),
        ('ENFERMERA', 'Enfermera'),
        ('AUX', 'Auxiliar'),
        ('PAC', 'Paciente'),
    )

    email = models.EmailField('Email', max_length=254, unique=True)
    nombre = models.CharField('Nombre', max_length=150)
    apellido = models.CharField('Apellido', max_length=150)
    role = models.CharField('Rol', max_length=10, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']


    def __str__(self):
        return f'{self.email} {self.role}'



class VerificationCode(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField('Codigo', max_length=6)

    class Meta:
        verbose_name = 'Codigo'
        verbose_name_plural = 'Codigos'

    def __str__(self):
        return f'Codigo de {self.user.email}'