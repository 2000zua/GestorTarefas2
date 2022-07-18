from django.db import models

# Create your models here.

class Tarefas(models.Model):
    OPCOES_STATUS = (
        ('concluido','Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado')
    )
    OPCOES_CATEGORIAS = (
        ('urgente', 'Urgente'),
        ('importante','Importante'),
        ('Precisa ser feito','Precisa ser feito')
    )

    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add = True)
    categorias = models.CharField(max_length=25, choices=OPCOES_CATEGORIAS, default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')
