from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Carro
from .serializers import CarroSerializer
from users.permissions import IsClienteReadOnlyOrFuncionario  # ✅ Nova permissão

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field = 'placa'
    
    # ✅ Define a permissão global correta
    permission_classes = [IsClienteReadOnlyOrFuncionario]

    # As actions personalizadas já herdam permission_classes do ViewSet,
    # então NÃO é necessário repetir permission_classes=[IsAuthenticated] nelas.
    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        carros = self.queryset.filter(status='disponivel')
        serializer = self.get_serializer(carros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def alugados(self, request):
        carros = self.queryset.filter(status='alugado')
        serializer = self.get_serializer(carros, many=True)
        return Response(serializer.data)