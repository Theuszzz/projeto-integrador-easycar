from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import PerfilCliente

#------------------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)
    primeiro_nome = serializers.CharField(source='first_name', required=True)  # mapeia first_name, campo obrigatorio
    is_staff = serializers.BooleanField(default=False, read_only=True)
    is_superuser = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'primeiro_nome' , 'is_staff' , 'senha', 'is_active' , 'is_superuser']

    def create(self, validated_data):

        first_name = validated_data.pop('first_name') # pega e remove o primeiro nome do dicionario
        senha = validated_data.pop('senha') # pega e remove senha do dicionario


        # cria usuarios
        cliente = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=first_name,
            password=senha,
            is_active=True,
            is_staff=False,
            is_superuser=False
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
