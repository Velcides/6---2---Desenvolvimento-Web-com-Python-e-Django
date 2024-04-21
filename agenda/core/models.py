from django.db import models
# Importando a classe de usuarios padrão.
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

# Criando a classe de eventos, passando como parametro models que fornece funções de criação de campos.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    # Pode ser nulo e em branco.]
    descricao = models.TextField(blank=True, null=True)
    # verbose altera o nome no django admin.
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    # Cria a data na hora da inserção.
    data_criacao = models.DateTimeField(auto_now=True)
    # Relacionando com a tabela de usuários.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # cascade deleta o user e tudo relacionado ao mesmo.

    # Nomeando a tabela com o nome evento, por padrão o nome é criado como nome do app + _ + nome da classe (core_evento).
    class Meta:
        db_table = 'evento'

    # Nomeando o evento criado com o titulo, sem esse tratamento o nome do objeto criado fica "Evento object(1)".
    def __str__(self):
        return self.titulo
    
    # Função para formatar o padrão de data na exibição.
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')
    
    # Retorna a data do evento para tela de edição
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False