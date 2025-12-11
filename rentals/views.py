from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from users import permissions
from .models import Aluguel
from .serializers import AluguelSerializer
from rest_framework import generics
from datetime import date
from users import permissions
from decimal import Decimal


@user_passes_test(permissions.IsFuncionarioOuSuperuser, login_url="no_permission")
class AlugarCarro(generics.ListCreateAPIView):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer

class AtualizarAluguel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer



    
        
        


    

   


