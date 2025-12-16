import django_filters
from .models import Aluguel

class AluguelFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data_inicio')
    data_fim = django_filters.DateFilter(field_name='data_fim')
    status = django_filters.CharFilter(field_name='status')
    
    carro = django_filters.NumberFilter(field_name='carro__id') #filtra pelo id
    cliente = django_filters.NumberFilter(field_name='perfil_cliente__id') # filtra pelo id

    class Meta:
        model = Aluguel
        fields = [
            'data_inicio',
            'data_fim',
            'status',
            'carro',
            'cliente',
        ]
