import secrets
#
import string
#
from .models import User, VerificationCode
#



def create_code(size=6, chars=string.ascii_uppercase + string.digits):
    code = []
    for _ in range(0, size):
        code.append(secrets.choice(chars))    
    return ''.join(code)


def create_user_verification_code(email, nombre, apellido, role):
    user = User.objects.create(
                email=email,
                nombre=nombre,
                apellido=apellido,
                role=role
            )
    
    new_code = create_code()

    codigo = VerificationCode.objects.create(
        user = user,
        code = new_code
    ) 

    return codigo