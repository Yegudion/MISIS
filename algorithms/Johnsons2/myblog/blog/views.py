# # blog/views.py
# from django.shortcuts import render
# # from .models import Post, Engineer
# from .models import Engineer

# # def post_list(request):
# #     posts = Post.objects.all()
# #     return render(request, 'blog/post_list.html', {'posts': posts})

# def engineer_list(request):
#     engineers = Engineer.objects.all()
#     return render(request, 'blog/engineer_list.html', {'engineers': engineers})

# blog/views.py

# from django.shortcuts import render
# from .models import  Engineer
# from .utils import johnson_scheduling

# def engineer_list(request):
#     engineers = Engineer.objects.all()
#     return render(request, 'blog/engineer_list.html', {'engineers': engineers})

# def schedule_tasks(request):
#     # Пример задач
#     tasks_list = [(3, 2), (1, 4), (5, 1), (2, 3), (4, 2)]
#     # Получаем оптимальное расписание
#     optimal_schedule = johnson_scheduling(tasks_list)
#     # Формируем данные для отображения
#     tasks_with_schedule = [(f"Задача {chr(65 + i)}", optimal_schedule[i]) for i in range(len(tasks_list))]
#     return render(request, 'blog/schedule_tasks.html', {'tasks_with_schedule': tasks_with_schedule})


# blog/views.py

from django.shortcuts import render
from .models import  Engineer, Task
from .utils import johnson_scheduling

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

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