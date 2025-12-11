from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import PerfilCliente

#------------------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'senha', 'is_active']

    def create(self, validated_data):
        # cria usuarios
        cliente = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['senha'],
            is_active=True
        )

        # adiciona automaticamente ao grupo "Clientes"
        grupo_cliente = Group.objects.get(name="Clientes")
        cliente.groups.add(grupo_cliente)
        cliente.save()
        return cliente
#--------------------------------------------------------------------
class PerfilClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        # querysetFilter=User.objects.filter(groups__name='Clientes'),
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = PerfilCliente
        fields = ['id', 'user', 'user_id', 'cnh', 'telefone', 'endereco']
