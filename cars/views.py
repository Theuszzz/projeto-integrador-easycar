from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Carro
from .serializers import CarroSerializer


class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()

    # Bloqueia todos os métodos de escrita (POST, PUT, PATCH, DELETE)
    http_method_names = ['get', 'head', 'options']

    # Rota personalizada: /api/carros/disponiveis/
    @action(detail=False, methods=['get'], url_path='disponiveis')
    def disponiveis(self, request):
        carros = self.queryset.filter(status='disponivel')
        serializer = self.get_serializer(carros, many=True)
        return Response(serializer.data)
