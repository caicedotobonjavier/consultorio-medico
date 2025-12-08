from django.shortcuts import render
#
from rest_framework.generics import CreateAPIView
#
from rest_framework.views import APIView
#
from .serializers import UserSerializer, ValidateCodeSerializer
#
from .models import User, VerificationCode
#
from .functions import create_code
#
from rest_framework.response import Response
#
from rest_framework import status
#
from .functions import create_user_verification_code
#
from django.db import transaction
# Create your views here.


class CreateUserApiView(APIView):

    def post(self, request, *args, **kwargs):
        
        with transaction.atomic():
            serializador = UserSerializer(data=request.data)
            serializador.is_valid(raise_exception=True)
                
            email = serializador.validated_data['email']
            nombre = serializador.validated_data['nombre']
            apellido = serializador.validated_data['apellido']
            role = serializador.validated_data['role']
                
            user_code = create_user_verification_code(
                email=email, 
                nombre=nombre, 
                apellido=apellido, 
                role=role
            )
            print(user_code.__dict__)

            return Response(
                {
                    'response' : "success",
                    'user_id' : user_code.user_id,
                    'user_code' : user_code.code,
                    'user_email' : User.objects.get(id=user_code.user_id).email,
                    'activate_user' : 'activa tu usuario en el siguiente link: http://127.0.0.1:8000/user-api/activate-user?id=USER_ID',
                    'required_data' : '"code" : "your_code"',
                    'method' : 'POST'
                },
                status=status.HTTP_201_CREATED
            )     


class VerficationCodeApiView(CreateAPIView):
    serializer_class = ValidateCodeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['id_user'] = self.request.query_params.get('id')
        return context

    def get(self, request, *args, **kwargs): 
        serializador = self.get_serializer(data=request.data)
        serializador.is_valid(raise_exception=True)

        id = self.request.query_params.get('id')

        user = User.objects.get(id=id)
        print(user)
        user.is_active = True
        user.is_staff = True
        user.save()
    
        return Response(
            {
                'response' : 'success',
                'estate_user' : user.is_active

            },
            status=status.HTTP_200_OK
        )