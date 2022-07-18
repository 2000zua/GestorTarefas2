from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .form import AdicionarTarefa, EditarTarefaForm

# Create your views here.
def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefas.objects.filter(status='pendente')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = AdicionarTarefa()

    return render(request,'tarefas/tarefas_pendentes.html',{'t_pendentes':tarefas_pendentes, 'form':form})


def concluir_tarefa(request, tarefas_id):
    tarefa = get_object_or_404(Tarefas, id=tarefas_id)
    tarefa.status = 'concluído'
    tarefa.save()
    return redirect('tarefas_pendentes_list')


def excluir_tarefa(request, tarefas_id):
    tarefa = get_object_or_404(Tarefas, id=tarefas_id)
    tarefa.delete()
    return redirect('tarefas_pendentes_list')


def adiar_tarefa(request, tarefas_id):
    tarefa = get_object_or_404(Tarefas, id=tarefas_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_pendentes_list')


def editar_tarefa(request, tarefas_id):
    tarefa = get_object_or_404(Tarefas, id=tarefas_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categorias = cd['categorias']
            tarefa.save()
            return redirect('tarefas_pendentes_list')
    else:
        form = EditarTarefaForm(initial = {'tarefa':tarefa.descricao, 'categorias':tarefa.categorias})
    return render(request, 'tarefas/editar_tarefa.html', {'tarefa':tarefa, 'form':form})


def tarefas_concluidas(request):
    tarefas_concluida = Tarefas.objects.filter(status='concluído')
    return render(request, 'tarefas/tarefas_concluidas.html', {'tarefas_concluida':tarefas_concluida})


def tarefas_adiadas_list(request):
    tarefas_adidas = Tarefas.objects.filter(status='adiado')
    return render(request, 'tarefas/tarefas_adiadas_list.html', {'tarefas_adiadas_list':tarefas_adidas})


def mover_para_tarefa(request, tarefas_id):
    tarefa = get_object_or_404(Tarefas, id=tarefas_id)
    tarefa.status = 'pendente'
    tarefa.save()
    return redirect('tarefas_adiadas_list')
