from rest_framework import serializers
from .models import Aluguel

class AluguelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluguel
        fields = ['id', 'carro', 'funcionario', 'data_inicio', 'data_fim','valor_total','status']

    
    def perform_create(self, validated_data):
        aluguel = validated_data

        data_inicio = validated_data['data_inicio']
        data_fim = validated_data['data_fim']
        carro = validated_data['carro']

        # Calcula dias alugados
        dias = (data_fim - data_inicio).days
        
        if dias <= 0:
            dias = 1  # garante pelo menos 1 dia

        # Calcula valor total
        valor_total = dias * carro.valor_diaria

        # Salva já com o valor calculado
        serializer.save(valor_total=valor_total)
