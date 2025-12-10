from rest_framework.permissions import BasePermission

class IsFuncionarioOuSuperuser(BasePermission):

# Permite que apenas usuários que pertençam ao grupo 'Funcionários' ou
# sejam superusuários acessem a view.
    
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (
            user.is_superuser or user.groups.filter(name='Funcionários').exists()
        )