from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Carro
from .serializers import CarroSerializer



class CarroViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarroSerializer
    lookup_field = 'placa' 

    # ----- QuerySet base -----
    def get_queryset(self):
        queryset = Carro.objects.all()

        # rota pública para disponíveis
        if self.action == 'disponiveis':
            return queryset.filter(status='disponivel')

        return queryset

    

    
