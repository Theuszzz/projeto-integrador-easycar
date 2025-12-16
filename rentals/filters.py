import django_filters
from .models import Aluguel

class AluguelFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data_inicio')
    data_fim = django_filters.DateFilter(field_name='data_fim')
    carro = django_filters.NumberFilter(field_name='carro__id') #filtra pelo id


    status = django_filters.ChoiceFilter(field_name='status',
        choices=[ 
            ('ativo', 'Ativo'),
            ('finalizado', 'Finalizado'),
            ('cancelado', 'Cancelado'),
        ],
        empty_label="Todos os status",  # texto para opcao vazia
        label="Status do aluguel"  
)

    cliente = django_filters.CharFilter(
        method='filter_cliente',
        label='Cliente (ID ou Nome de Usuário)'
    )

    funcionario = django_filters.CharFilter(  
        method='filter_funcionario',
        label='Funcionário (ID ou Nome de Usuário)'
    )

    def filter_cliente(self, queryset, name, value):
        # tenta filtrar por ID 
        if value.isdigit():
            return queryset.filter(perfil_cliente__id=value)
        # se nao for numero, filtra por nome
        return queryset.filter(
            perfil_cliente__user__username__icontains=value
        )
    
    def filter_funcionario(self, queryset, name, value):
        if value.isdigit():
            return queryset.filter(funcionario__id=value)
        return queryset.filter(
            funcionario__username__icontains=value 
    )

    class Meta:
        model = Aluguel
        fields = [
            'data_inicio',
            'data_fim',
            'status',
            'carro',
            'cliente',
            'funcionario',
        ]
