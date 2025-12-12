from rest_framework import serializers
from .models import Aluguel

class AluguelSerializer(serializers.ModelSerializer):
    valor_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = Aluguel
        fields = ['id', 'perfil_cliente', 'carro', 'funcionario', 'data_inicio', 'data_fim','status', 'valor_total']

    
    def validate(self, aluguel):
        data_inicio = aluguel["data_inicio"]
        data_fim = aluguel["data_fim"]

        if data_inicio and data_fim:
            if data_fim < data_inicio:
                raise serializers.ValidationError({
                    "data_fim": "A data de fim não pode ser menor que a data de início."
                })

        return aluguel


