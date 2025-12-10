from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.medico.models import Medico
#
from applications.paciente.models import Paciente
# Create your models here.

class Cita(TimeStampedModel):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_cita = models.DateField('Fecha Cita')
    hora_cita = models.TimeField('Hora Cita')
    duracion_minutos = models.IntegerField(default=30)
    motivo_cita = models.TextField('Motivo Cita')
    estado = models.CharField(
        'Estado Cita',
        max_length=20,
        choices=[
            ('AGENDADA', 'Agendada'),
            ('CANCELADA', 'Cancelada'),
            ('COMPLETADA', 'Completada'),
        ],
        default='AGENDADA'
    )


    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['id']
    


    def __str__(self):
        return f'Cita {self.fecha_cita} {self.hora_cita} - {self.medico.user.nombre}'