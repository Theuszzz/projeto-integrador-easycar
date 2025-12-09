from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    ano = models.IntegerField()
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alugado', 'Alugado'),    
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')

    def alterar_status(self, novo_status):
        if novo_status in dict(self.STATUS_CHOICES):
            self.status = novo_status
            self.save()
        else:
            raise ValueError("Status inválido")

    def __str__(self):
        return f"{self.modelo} ({self.placa})"