from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, permissions, serializers
from .models import PerfilCliente
from .serializers import PerfilClienteSerializer
from .serializers import UserSerializer
from users.permissions import IsFuncionarioOuSuperuser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rentals.models import Aluguel
from rentals.serializers import AluguelSerializer
# Temporário
class AluguelSerializerTeste(serializers.Serializer):
    # Mock básico para testes
    id = serializers.IntegerField()
    username = serializers.CharField(source='perfil_cliente.user.username')
    status = serializers.CharField()
    valor_total = serializers.DecimalField(max_digits=10, decimal_places=2)
Aluguel = None

# CRUD de usuários (somente funcionários ou superuser)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsFuncionarioOuSuperuser]

# classe para visualizar os perfis dos clientes
class PerfilClienteViewSet(viewsets.ModelViewSet):
    # usa o serializador de perfil de cliente
    serializer_class = PerfilClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsFuncionarioOuSuperuser]

    def get_queryset(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        # pega o usuário logado
        user = self.request.user

        # se for staf, retorna todos os perfis
        # if user.is_staff:
        return PerfilCliente.objects.select_related('user').all()
        
        # return []
    
    # rota api/perfis-clientes/{id}/alugueis
    @action(detail=True, methods=['get'])
    def alugueis(self, request, pk=None):
        perfil_cliente = self.get_object()
        alugueis = perfil_cliente.get_historico_alugueis()
        serializer = AluguelSerializer(alugueis, many=True)
        return Response(serializer.data)
    
class MeusAlugueisView(viewsets.ReadOnlyModelViewSet):
    # usa o serializador de perfil de cliente
    serializer_class = AluguelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        # pega o usuário logado
        user = self.request.user

        # se for staf, retorna todos os perfis
        # if user.is_staff:
        #     return PerfilCliente.objects.select_related('user').all()
        
        # return PerfilCliente.objects.select_related('user').filter(user=user)
    
        if hasattr(user, 'perfilcliente'):
            perfil_cliente = user.perfilcliente
            return perfil_cliente.alugueis.all()
        return []