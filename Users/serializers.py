from rest_framework import serializers

class UserSerializer(serializers.Serializer):
     name = serializers.CharField(required= False)
     email = serializers.EmailField(required= True)
     password = serializers.CharField(required= True)    