def johnson_algorithm(jobs):
    # Разделение задач на две группы
    n = len(jobs)
    left_sequence = []
    right_sequence = []

    while jobs:
        # Находим минимальное время среди всех задач на обеих машинах
        min_job = min(jobs, key=lambda x: min(x[1][0], x[1][1]))

        # Разделение на группы и исключение выбранной задачи
        if min_job[1][0] <= min_job[1][1]:
            left_sequence.append(min_job[0])
        else:
            right_sequence.insert(0, min_job[0])

        jobs.remove(min_job)

    # Объединяем левую и правую последовательности
    return left_sequence + right_sequence

# Пример данных задач
jobs = [
    ('A', (3, 2)),
    ('B', (5, 4)),
    ('C', (2, 3)),
    ('D', (4, 6)),
    ('E', (6, 1))
]

# Применение алгоритма Джонсона
optimal_sequence = johnson_algorithm(jobs)

print("Оптимальная последовательность задач:", optimal_sequence)

# Расчет времени выполнения на машинах M1 и M2
def calculate_makespan(sequence, jobs_dict):
    m1_time = 0
    m2_time = 0
    for job in sequence:
        m1_time += jobs_dict[job][0]
        if m1_time < m2_time:
            m1_time = m2_time
        m2_time = m1_time + jobs_dict[job][1]
    return m2_time

# Преобразование списка задач в словарь для удобства расчетов
jobs_dict = {job[0]: job[1] for job in jobs}

# Вычисление общего времени выполнения
makespan = calculate_makespan(optimal_sequence, jobs_dict)

print("Общее время выполнения (makespan):", makespan)
