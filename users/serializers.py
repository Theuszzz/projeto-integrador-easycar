from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilCliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class PerfilClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PerfilCliente
        fields = ['id', 'user', 'cnh', 'telefone', 'endereco']
