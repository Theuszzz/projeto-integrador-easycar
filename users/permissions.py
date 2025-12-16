from rest_framework.permissions import BasePermission

class IsFuncionarioOuSuperuser(BasePermission):

# Permite que apenas usuários que pertençam ao grupo 'Funcionários' ou
# sejam superusuários acessem a view.
    
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (
            user.is_superuser or user.groups.filter(name='Funcionários').exists()
        )
from rest_framework import permissions

class IsClienteReadOnlyOrFuncionario(permissions.BasePermission):
   
    def has_permission(self, request, view):
        # Primeiro, exige autenticação
        if not request.user or not request.user.is_authenticated:
            return False

        # Se for um método de leitura (GET, HEAD, OPTIONS), permite qualquer autenticado
        if request.method in permissions.SAFE_METHODS:
            return True

        # Para métodos de escrita (POST, PUT, PATCH, DELETE), só permite funcionários ou superusers
        return request.user.is_staff or request.user.is_superuser