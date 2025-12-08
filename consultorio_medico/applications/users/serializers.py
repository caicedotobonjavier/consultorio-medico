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

    password = serializers.CharField(
        help_text = "Ingrese su contraseña",
        required = True
    )

    confirm_password = serializers.CharField(
        help_text = "Confirme su contraseña",
        required = True
    )

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('La contraseña debe tener minimo 8 caracteres')
        return value

    def validate(self, data): 
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        return data



class ValidateCodeSerializer(serializers.Serializer):
    code = serializers.CharField(
        help_text = "Codigo para activar user",
        required = True
    )

    def validate(self, attrs):
        user_id = self.context.get('id_user')
        print(user_id)
        user_update = User.objects.get(id=user_id)
        print(user_update)
        if not VerificationCode.objects.filter(user=user_update, code=attrs['code']).exists():
            raise serializers.ValidationError('El codigo no pertenece al usaurio')        
        return attrs
    

    def validate_code(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('El codigo no tiene la longitud correcta')        
        return value


    