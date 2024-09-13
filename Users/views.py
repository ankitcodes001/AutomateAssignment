from django.shortcuts import render
from Features.urls import *
# Crear views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Users.services.user_services import UserServices
from Users.serializers import UserSerializer
from drf_yasg import openapi

# Define the request schema for registration and login
register_request_body = openapi.Schema(
    title='User Registration',
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='User name'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
    },
    required=['name', 'email', 'password']
)

login_request_body = openapi.Schema(
    title='User Login',
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
    },
    required=['email', 'password']
)

# Define the response schema
success_response = openapi.Response(
    description='Operation was successful',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
            'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token'),
        },
    )
)

error_response = openapi.Response(
    description='Error response',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
        },
    )
)

class UserRegistrationAPIView(APIView):
    @swagger_auto_schema(
        request_body=register_request_body,
        responses={
            201: success_response,
            400: error_response,
            500: error_response
        }
    )
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
    @swagger_auto_schema(
        request_body=login_request_body,
        responses={
            200: openapi.Response(
                description='Login successful',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token'),
                    }
                )
            ),
            400: error_response,
            500: error_response
        }
    )
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
    @swagger_auto_schema(
        responses={
            200: success_response,
            400: error_response,
            500: error_response
        }
    )
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return Response({'error': 'Please provide a valid token.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            UserServices.logout_user(token)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
