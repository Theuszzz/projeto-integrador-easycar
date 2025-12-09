from django.contrib import admin
from .models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa','ano','valor_diaria', 'status')
    list_filter = ('status',)
    search_fields = ('modelo', 'placa','ano','status')