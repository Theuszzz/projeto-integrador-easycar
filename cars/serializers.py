from rest_framework import serializers
from .models import Carro

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id','modelo', 'placa', 'ano', 'valor_diaria', 'status']
        read_only_fields = ['status']  # impede alterar direto

class AlterarStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Carro.STATUS_CHOICES)

    def update(self, instance, validated_data):
        status = validated_data.get('status')
        if status == 'alugado':
            instance.marcar_como_alugado()
        elif status == 'disponivel':
            instance.marcar_como_disponivel()
        return instance

      
