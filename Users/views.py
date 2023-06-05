from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Users.services.user_services import UserServices
from Users.serializers import UserSerializer


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            UserServices.register_user(serializer.validated_data['name'], serializer.validated_data['password'], serializer.validated_data['email'])
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = UserServices.login_user(serializer.validated_data['email'], serializer.validated_data['password'])
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'token': token}, status=status.HTTP_200_OK)

class UserLogoutAPIView(APIView):
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return Response({'error': 'Please provide a valid token.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            UserServices.logout_user(token)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
