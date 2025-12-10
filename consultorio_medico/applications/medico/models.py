from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.users.models import User
# Create your models here.

class Especialidad(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=120)


    class Meta:
        verbose_name = 'Especilidad'
        verbose_name_plural = 'Especialidades'
        ordering = ['id']
    


    def __str__(self):
        return self.nombre



class Medico(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    registro_profesional = models.CharField('Registro Profesional', max_length=50, default="Pendiente")


    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        ordering = ['id']
    

    def __str__(self):
        return f'{self.user.nombre} {self.user.apellido} - {self.especialidad}'