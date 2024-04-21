from django.contrib import admin
from core.models import Evento

# Register your models here.

# Alterando a visualização da listangem no django admin.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    # Criando filtros.
    list_filter = ('usuario', 'data_evento','id',)
    
# Registrando a tabela evento e sua visualização.
admin.site.register(Evento, EventoAdmin)

