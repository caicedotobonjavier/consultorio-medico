from rest_framework import serializers
#
from .models import User, VerificationCode

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



class ValidateCodeSerializer(serializers.Serializer):
    code = serializers.CharField(
        help_text = "Codigo para activar user",
        required = True
    )

    def validate(self, attrs):
        user_id = self.context.get('id_user')
        print(user_id)
        user = User.objects.filter(id=user_id)
        user_code = VerificationCode.objects.filter(code=attrs['code'])
        print(user, user_code)
        return attrs
    

    def validate_code(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('El codigo no tiene la longitud correcta')        
        return value


    