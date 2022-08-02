from dataclasses import fields
from rest_framework import serializers
from authApp.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['identificacion','nombre','apellido','username','password','email']

    def create (self, validated_data): #Deserializacion JSON a Objeto Python
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj): # Serializacion objeto Python a JSON
        user = User.objects.get(id = obj.id)
        return {
            'identificacion':user.identificacion,
            'apellido': user.apellido,
            'username': user.username,
            'email': user.email,
        }

        