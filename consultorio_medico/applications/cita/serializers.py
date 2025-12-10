from rest_framework import serializers
#
from .models import Cita
#
from applications.paciente.models import Paciente
#
from applications.medico.models import Medico
#
from datetime import date
#
from datetime import datetime, timedelta
#
from django.utils import timezone



class CitaSerializer(serializers.Serializer):
    medico = serializers.PrimaryKeyRelatedField(
        queryset = Medico.objects.all(),
        help_text = 'Medico disponible',
        required = True
    )

    paciente = serializers.PrimaryKeyRelatedField(
        queryset = Paciente.objects.all(),
        help_text = 'Paciente',
        required = True
    )

    fecha_cita = serializers.DateField(
        help_text = 'Seleccione fecha disponible de atencion',
        default = date.today()
    )

    hora_cita = serializers.TimeField(
        help_text = 'Seleccione hora disponible de atencion',
        required = True
    )

    motivo_cita = serializers.CharField(
        help_text = 'Ingrese motivo por el cual consulta',
        required = True
    )


    def validate(self, data):
        medico = data['medico']
        fecha_cita = data['fecha_cita']
        hora_cita = data['hora_cita']

        # -------------------------
        # Crear datetime aware
        # -------------------------
        cita_inicio = datetime.combine(fecha_cita, hora_cita)
        if timezone.is_naive(cita_inicio):
            cita_inicio = timezone.make_aware(cita_inicio)

        # Duración (si no viene en request → 30)
        cita_duracion = data.get('duracion_minutos', 30)
        cita_fin = cita_inicio + timedelta(minutes=cita_duracion)

        # -------------------------
        # Validar colisión con otras citas
        # -------------------------
        citas_existentes = Cita.objects.filter(
            medico=medico,
            fecha_cita=fecha_cita,
            estado__in=['AGENDADA', 'COMPLETADA']
        )

        for cita in citas_existentes:
            cita_existente_inicio = datetime.combine(cita.fecha_cita, cita.hora_cita)
            if timezone.is_naive(cita_existente_inicio):
                cita_existente_inicio = timezone.make_aware(cita_existente_inicio)

            cita_existente_fin = (
                cita_existente_inicio +
                timedelta(minutes=cita.duracion_minutos)
            )

            # Chequeo de solapamiento
            if cita_inicio < cita_existente_fin and cita_fin > cita_existente_inicio:
                raise serializers.ValidationError({
                    'hora_cita': (
                        f'El médico ya tiene una cita a las '
                        f'{cita.hora_cita.strftime("%H:%M")} '
                        f'({cita.duracion_minutos} minutos).'
                    )
                })

        # -------------------------
        # Validación: no permitir citas en el pasado
        # -------------------------
        if cita_inicio < timezone.now():
            raise serializers.ValidationError({
                'hora_cita': 'No se puede agendar una cita en el pasado.'
            })

        return data
