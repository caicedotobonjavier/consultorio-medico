from django.shortcuts import render
#
from applications.paciente.models import Paciente
#
from applications.users.models import User
#
from .serializers import CitaSerializer
#
from rest_framework.views import APIView
#
from rest_framework.generics import CreateAPIView
#
from rest_framework.response import Response
#
from .functions import registrar_cita
# Create your views here.


class CreateCitaApiView(CreateAPIView):
    serializer_class = CitaSerializer

    def create(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        print(serializador.__dict__)

        medico = serializador.validated_data['medico']
        paciente = serializador.validated_data['paciente']
        fecha_cita = serializador.validated_data['fecha_cita']
        hora_cita = serializador.validated_data['hora_cita']
        motivo_cita = serializador.validated_data['motivo_cita']

        register_cita = registrar_cita(
            medico = medico,
            paciente = paciente,
            fecha_cita = fecha_cita,
            hora_cita = hora_cita,
            motivo_cita = motivo_cita
        )

        print(register_cita)

        return Response(
            {
                'mensaje' : 'success',
                'paciente' : f'{register_cita.paciente.user.nombre} {register_cita.paciente.user.apellido}',
                'fecha_cita' : register_cita.fecha_cita,
                'hora_cita' : register_cita.hora_cita,
            }
        )

