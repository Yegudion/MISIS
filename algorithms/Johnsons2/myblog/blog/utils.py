# blog/utils.py

def johnson_scheduling(tasks):
    """
    Распределение задач между двумя инженерами с использованием алгоритма Джонсона.

    :param tasks: Список объектов Task
    :return: Оптимальное расписание для инженеров
    """
    # Вычисляем время обработки для каждой задачи
    processing_times = [(task.time_machine_1 + task.time_machine_2, task.id) for task in tasks]

    # Сортируем задачи по возрастанию времени обработки
    sorted_tasks = sorted(processing_times)

    # Распределяем задачи на станки
    schedule = {}
    for i in range(len(sorted_tasks)):
        _, task_id = sorted_tasks[i]
        if i < len(sorted_tasks) // 2:
            schedule[task_id] = "Инженер 1"
        else:
            schedule[task_id] = "Инженер 2"

    return schedule
