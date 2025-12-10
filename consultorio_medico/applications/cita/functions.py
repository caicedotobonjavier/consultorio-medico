from .models import Cita
#
from django.db import transaction
#
from django.db import transaction, IntegrityError
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException

def registrar_cita(**datos):
    try:
        with transaction.atomic():
            cita = Cita.objects.filter(paciente=datos['paciente'], estado='AGENDADA').exists()
            if not cita:
                datos_cita = Cita.objects.create(
                    medico = datos['medico'],
                    paciente = datos['paciente'],
                    fecha_cita = datos['fecha_cita'],
                    hora_cita = datos['hora_cita'],
                    motivo_cita = datos['motivo_cita'],
                )
                return datos_cita
            else:
                raise ValidationError({
                    'paciente': [
                        'Ya tiene una cita agendada. '
                        'Estado actual: AGENDADA'
                    ]
                })    
    except ValidationError:
        raise  # Deja que DRF maneje esta excepción
    except Exception as e:
        raise ValidationError({
            'non_field_errors': [f'Error al registrar cita: {str(e)}']
        })
