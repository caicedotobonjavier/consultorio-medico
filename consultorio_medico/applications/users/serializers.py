from rest_framework import serializers
#
from .models import User

class UserSerializer(serializers.Serializer):  
    email = serializers.EmailField(
        help_text = "Ingrese su email",
        required = True
    )
    nombre = serializers.CharField(
        help_text = "Ingrese sus nombres",
        required = True
    )
    apellido = serializers.CharField(
        help_text = "Ingrese sus apellidos",
        required = True
    )
    role = serializers.ChoiceField(
        choices = User.ROLE_CHOICES,
        help_text = "Roles disponibles: Administrador, Especialista, Medico, Enfermera, Auxiliar, Paciente"
    )