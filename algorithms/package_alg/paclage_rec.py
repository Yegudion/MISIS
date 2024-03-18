"""
  Рекурсивная функция для решения задачи о рюкзаке.

  Args:
      items: Список кортежей (вес, ценность) для каждого предмета.
      capacity: Вместимость рюкзака.

  Returns:
      Кортеж (максимальная ценность, список выбранных предметов).
"""


def knapsack(items, capacity):


  # Базовый случай: рюкзак пустой или нет предметов
  if capacity == 0 or not items:
    return 0, []

  item, *rest = items
  weight, value = item

  # Взять предмет
  if weight <= capacity:
    take_item, taken_items = knapsack(rest, capacity - weight)
    take_value = value + take_item

  # Не брать предмет
  skip_item, skipped_items = knapsack(rest, capacity)

  # Выбрать вариант с максимальной ценностью
  if take_value > skip_item:
    return take_value, [item] + taken_items
  else:
    return skip_item, skipped_items

# Пример использования
items = [(5, 10), (4, 7), (3, 6), (2, 5)]
capacity = 10

max_value, taken_items = knapsack(items, capacity)

print(f"Максимальная ценность: {max_value}")
print(f"Взятые предметы: {taken_items}")