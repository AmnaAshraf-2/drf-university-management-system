from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from rest_framework.authtoken.models import Token
from .serializers import (
    RegisterSerializer, LogInSerializer,
    UserSerializer)


class RegisterAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.create(user=user)

        user_data = UserSerializer(user).data
        return Response({
            'user': user_data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = LogInSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            return Response({
                'user': user_serializer.data,
                'token': token.key
            })
        else:
            return Response({'detail': 'Invalid Credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)


