"""
  Жадный алгоритм для задачи о рюкзаке.

  Args:
    items: Список кортежей (вес, ценность) для каждого предмета.
    capacity: Вместимость рюкзака.

  Returns:
    Список выбранных предметов.
"""

# 1. Сортировка предметов по удельной ценности (ценность/вес).
# 2. Список выбранных предметов.
# 3. Перебор предметов. 
#   a. Если предмет помещается в рюкзак.
#   b. Увеличение текущего веса, .
def greedy_knapsack(items, capacity):

 
  items.sort(key=lambda item: item[1] / item[0], reverse=True)

  
  selected_items = []

  
  current_weight = 0

  
  for item in items:
    if current_weight + item[0] <= capacity:
      selected_items.append(item)
      
      current_weight += item[0]

  return selected_items

# Пример
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50

selected_items = greedy_knapsack(items, capacity)

# Вывод
for item in selected_items:
  print(f"Предмет: {item[0]} - {item[1]}")

print(f"Общий вес: {sum(item[0] for item in selected_items)}")
print(f"Общая ценность: {sum(item[1] for item in selected_items)}")

