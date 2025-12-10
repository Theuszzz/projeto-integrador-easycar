from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Carro
from .serializers import CarroSerializer

from users.permissions import IsFuncionarioOuSuperuser
from rest_framework.permissions import IsAuthenticated


class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()
    permission_classes = [IsAuthenticated, IsFuncionarioOuSuperuser]

    # Rota personalizada: /api/carros/disponiveis/
    @action(detail=False, methods=['get'], url_path='disponiveis')
    def disponiveis(self, request):
        carros = self.queryset.filter(status='disponivel')
        serializer = self.get_serializer(carros, many=True)
        return Response(serializer.data)
