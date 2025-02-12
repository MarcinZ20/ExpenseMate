from versioning.AcceptHeaderVersioning import AcceptHeaderVersioning
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MyTokenObtainPairSerializer
from users import models
from users import serializers 

class MyTokenObtainPairView(TokenObtainPairView):
    versioning_class = AcceptHeaderVersioning
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if models.User.objects.filter(email=email).exists():
            return Response({'error': 'Account with this email address already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        new_user = models.User.objects.create_user(email=email, password=password)
        
        return Response({
            'user': serializers.UserSerializer(new_user).data
        }, status=status.HTTP_201_CREATED)