import secrets
#
import string


def create_code(size=6, chars=string.ascii_uppercase + string.digits):
    code = []
    for _ in range(0, size):
        code.append(secrets.choice(chars))
    
    return ''.join(code)