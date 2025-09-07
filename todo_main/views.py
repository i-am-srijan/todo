from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    # print(task)
    context={
        'tasks1': tasks,
    }
    return render(request, 'home.html', context)