# blog/views.py

from django.shortcuts import render
from .models import  Engineer, Task
from .utils import johnson_scheduling

def engineer_list(request):
    engineers = Engineer.objects.all()
    return render(request, 'blog/engineer_list.html', {'engineers': engineers})

def schedule_tasks(request):
    tasks = Task.objects.all()
    # Получаем оптимальное расписание
    optimal_schedule = johnson_scheduling(tasks)
    # Формируем данные для отображения
    tasks_with_schedule = [(task.name, optimal_schedule[task.id]) for task in tasks]
    return render(request, 'blog/schedule_tasks.html', {'tasks_with_schedule': tasks_with_schedule})