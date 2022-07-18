from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_pendentes_list, name='tarefas_pendentes_list'),
    path('<int:tarefas_id>/concluir/', views.concluir_tarefa, name='concluir_tarefa' ),
    path('<int:tarefas_id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:tarefas_id>/adiar/', views.adiar_tarefa, name='adiar_tarefa'),
    path('<int:tarefas_id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('concluidas/', views.tarefas_concluidas, name='tarefas_concluidas'),
    path('adiadas/', views.tarefas_adiadas_list, name='tarefas_adiadas_list'),
    path('<int:tarefas_id>/mover_para_lista_de_tarefa/', views.mover_para_tarefa, name='mover_para_tarefa')
]
