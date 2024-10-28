from django.shortcuts import render


# Create your views here.
def lista_tarefas(request):
    tarefas = ["Estudar django", "Criar um projeto", "Revisar o conteúdo"]
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
