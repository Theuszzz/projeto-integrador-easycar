from django.db import models
from django.contrib.auth.models import User
from users.models import PerfilCliente
from cars.models import Carro

class Aluguel(models.Model):
    # related_name serve para facilitar o acesso reverso
    perfil_cliente = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE, related_name='alugueis')
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT, related_name='alugueis')
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='alugueis_registrados')
    
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    def save(self, *args, **kwargs):
        # Só calcula se datas e carro existirem
        if self.data_inicio and self.data_fim and self.carro:
            dias = (self.data_fim - self.data_inicio).days
            if dias <= 0:
                dias = 1
            
            self.valor_total = dias * self.carro.valor_diaria

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Aluguel {self.id} - {self.carro.modelo}"