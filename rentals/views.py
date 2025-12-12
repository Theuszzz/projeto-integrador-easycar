from django.shortcuts import render
from .models import Aluguel
from .serializers import AluguelSerializer
from rest_framework import viewsets, serializers
from users.permissions import IsFuncionarioOuSuperuser


class AlugarViewSet(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    permission_classes = [IsFuncionarioOuSuperuser]

 
    
       










    
        
        


    

   


