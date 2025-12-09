from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import PerfilCliente
from .serializers import PerfilClienteSerializer

# classe para visualizar os perfis dos clientes
class PerfilClienteViewSet(viewsets.ReadOnlyModelViewSet):
    # usa o serializador de perfil de cliente
    serializer_class = PerfilClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        # pega o usuário logado
        user = self.request.user

        # se for staf, retorna todos os perfis
        if user.is_staff:
            return PerfilCliente.objects.select_related('user').all()
        
        return PerfilCliente.objects.select_related('user').filter(user=user)