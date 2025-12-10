from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.users.models import User
# Create your models here.


class Paciente(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField('Fecha Nacimiento', null=True, blank=True)
    telefono = models.CharField('Telefono', max_length=20, null=True, blank=True)


    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['id']
    

    def __str__(self):
        return f'{self.user.nombre} {self.user.apellido}'

