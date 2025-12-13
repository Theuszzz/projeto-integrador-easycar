from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import PerfilCliente

#------------------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False)
    primeiro_nome = serializers.CharField(source='first_name', required=False)  # mapeia first_name
    is_staff = serializers.BooleanField(default=False, read_only=True)
    is_superuser = serializers.BooleanField(default=False, read_only=True)
    grupo = serializers.SerializerMethodField() 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'primeiro_nome' , 'senha', 'is_active',  'is_staff'  , 
                  'is_superuser' , 'grupo']


    def get_fields(self):
        fields = super().get_fields()
        
        # Se for criação (POST), torna obrigatório
        if self.context.get('request') and self.context['request'].method == 'POST':
            fields['senha'].required = True
            fields['primeiro_nome'].required = True
        
        return fields
    
    def get_grupo(self, obj):
        # retorna apenas o primeiro grupo do usuario (ou None se nao tiver grupo)
        grupos = obj.groups.all()
        return grupos[0].name if grupos else None

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
    
    def update(self, instance, validated_data):
     # atualiza a senha somente se foi fornecida
        nova_senha = validated_data.get('senha', None)
        if nova_senha:
            instance.set_password(nova_senha)
            
        # chama o update da api para atualizar os outros campos normalmente
        return super().update(instance, validated_data)       
      
    

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
