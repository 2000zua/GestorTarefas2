from django.contrib import admin
from .models import Tarefas

# Register your models here.

class AdminTarefa(admin.ModelAdmin):
    list_display = ('descricao', 'criacao','categorias', 'status')

admin.site.register(Tarefas, AdminTarefa)
