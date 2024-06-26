def johnson_scheduling(tasks):
    """
    Распределение задач между двумя инженерами с использованием алгоритма Джонсона.

    :param tasks: Список задач в формате [(время_на_станке_1, время_на_станке_2), ...]
    :return: Оптимальное расписание для инженеров
    """
    # Вычисляем время обработки для каждой задачи
    processing_times = [(task[0] + task[1], i) for i, task in enumerate(tasks)]

    # Сортируем задачи по возрастанию времени обработки
    sorted_tasks = sorted(processing_times)

    # Распределяем задачи на станки
    schedule = [None] * len(tasks)
    for i in range(len(sorted_tasks)):
        _, task_index = sorted_tasks[i]
        if i < len(sorted_tasks) // 2:
            schedule[task_index] = "Инженер 1"
        else:
            schedule[task_index] = "Инженер 2"

    return schedule

# Пример задач
tasks_list = [(3, 2), (1, 4), (5, 1), (2, 3), (4, 2)]

# Получаем оптимальное расписание
optimal_schedule = johnson_scheduling(tasks_list)

# Выводим результат
for i, task in enumerate(optimal_schedule):
    print(f"Задача {chr(65 + i)}: {task}")
