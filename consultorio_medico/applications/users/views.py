from django.shortcuts import render
#
from rest_framework.generics import CreateAPIView
#
from .serializers import UserSerializer
#
from .models import User, VerificationCode
#
from .functions import create_code
#
from rest_framework.response import Response
#
from rest_framework import status
# Create your views here.


class CreateUserApiView(CreateAPIView):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        email = serializador.validated_data['email']
        nombre = serializador.validated_data['nombre']
        apellido = serializador.validated_data['apellido']
        role = serializador.validated_data['role']
        #creo el codigo
        code = create_code()
        user = User.objects.create(
            email=email,
            nombre=nombre,
            apellido=apellido,
            role=role,
        )

        codigo = VerificationCode.objects.create(
            user = user,
            code = code
        )    


        return Response(
            {
                'response' : "success",
                'email' : user.email,
                'role' : user.role,
                'code' : codigo.code
            },
            status=status.HTTP_201_CREATED
        )