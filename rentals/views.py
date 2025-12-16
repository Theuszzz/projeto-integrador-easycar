from django.shortcuts import render
from .models import Aluguel
from .serializers import AluguelSerializer
from rest_framework import viewsets, serializers
from users.permissions import IsFuncionarioOuSuperuser
from .filters import AluguelFilter 


class AlugarViewSet(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    permission_classes = [IsFuncionarioOuSuperuser]
    filterset_class = AluguelFilter #define quais campos podem ser filtrados



    
       










    
        
        


    

   


