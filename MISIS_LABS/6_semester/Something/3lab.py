from collections import deque, defaultdict
import random
import time

class Graph:
    def __init__(self, b, d):
        self.b = b  # коэффициент ветвления
        self.d = d  # глубина
        self.graph = defaultdict(list)
        self._build_tree()

    def _build_tree(self):
        """Строит дерево с коэффициентом ветвления b и глубиной d."""
        nodes_at_level = [0]  # корень дерева имеет номер 0
        node_id = 0
        
        for level in range(1, self.d + 1):
            next_level_nodes = []
            for parent in nodes_at_level:
                for _ in range(self.b):
                    node_id += 1
                    self.graph[parent].append(node_id)
                    next_level_nodes.append(node_id)
            nodes_at_level = next_level_nodes

    def bfs(self, start, target):
        """Поиск в ширину (BFS) с подсчётом итераций."""
        visited = set()
        queue = deque([[start]])
        iterations = 0
        
        if start == target:
            return [start], 1, 0
        
        while queue:
            iterations += 1
            path = queue.popleft()
            node = path[-1]
            
            if node not in visited:
                neighbors = self.graph[node]
                random.shuffle(neighbors)
                
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    if neighbor == target:
                        return new_path, iterations, len(new_path)
                    queue.append(new_path)
                visited.add(node)
        return None, iterations, 0

    def dfs(self, start, target):
        """Поиск в глубину (DFS) с подсчётом итераций."""
        visited = set()
        stack = [[start]]
        iterations = 0
        
        if start == target:
            return [start], 1, 0
        
        while stack:
            iterations += 1
            path = stack.pop()
            node = path[-1]
            
            if node == target:
                return path, iterations, len(path)
            
            if node not in visited:
                visited.add(node)
                neighbors = self.graph[node]
                random.shuffle(neighbors)
                
                for neighbor in reversed(neighbors):  # для корректного порядка в стеке
                    if neighbor not in visited:
                        stack.append(path + [neighbor])
        return None, iterations, 0

    def bidirectional_search(self, start, target):
        """Двунаправленный поиск с подсчётом итераций."""
        if start == target:
            return [start], 1, 0
        
        forward_queue = deque([[start]])
        backward_queue = deque([[target]])
        forward_visited = {start: [start]}
        backward_visited = {target: [target]}
        iterations = 0
        
        while forward_queue and backward_queue:
            iterations += 1
            
            # Шаг прямого поиска
            if forward_queue:
                forward_path = forward_queue.popleft()
                forward_node = forward_path[-1]
                
                if forward_node in backward_visited:
                    backward_path = backward_visited[forward_node]
                    full_path = forward_path + backward_path[-2::-1]
                    return full_path, iterations, len(full_path)
                
                for neighbor in self.graph[forward_node]:
                    if neighbor not in forward_visited:
                        new_path = forward_path + [neighbor]
                        forward_visited[neighbor] = new_path
                        forward_queue.append(new_path)
            
            # Шаг обратного поиска
            if backward_queue:
                backward_path = backward_queue.popleft()
                backward_node = backward_path[-1]
                
                if backward_node in forward_visited:
                    forward_path = forward_visited[backward_node]
                    full_path = forward_path + backward_path[-2::-1]
                    return full_path, iterations, len(full_path)
                
                parents = [p for p in self.graph if backward_node in self.graph[p]]
                for parent in parents:
                    if parent not in backward_visited:
                        new_path = backward_path + [parent]
                        backward_visited[parent] = new_path
                        backward_queue.append(new_path)
        
        return None, iterations, 0

    def count_connected_nodes(self, node, n):
        """Подсчитывает количество вершин, связанных с заданной на расстоянии <= n."""
        visited = set()
        queue = deque([(node, 0)])
        count = 0
        
        while queue:
            current_node, distance = queue.popleft()
            if distance > n:
                continue
            if current_node not in visited:
                visited.add(current_node)
                count += 1
                for neighbor in self.graph[current_node]:
                    queue.append((neighbor, distance + 1))
        return count - 1  # исключаем саму вершину

# Параметры графа
b = 5  # коэффициент ветвления
d = 9  # глубина

# Создаем граф
random.seed(42)  # для воспроизводимости
graph = Graph(b, d)

# Выбираем произвольную вершину с глубиной > 3 (например, 15)
target_node = 12367
start_node = 0

# Тестируем BFS
start_time = time.time()
bfs_path, bfs_iterations, bfs_length = graph.bfs(start_node, target_node)
bfs_time = time.time() - start_time

# Тестируем DFS
start_time = time.time()
dfs_path, dfs_iterations, dfs_length = graph.dfs(start_node, target_node)
dfs_time = time.time() - start_time

# Тестируем двунаправленный поиск
start_time = time.time()
bidirectional_path, bidirectional_iterations, bidirectional_length = graph.bidirectional_search(start_node, target_node)
bidirectional_time = time.time() - start_time

# Выводим результаты
print(f"BFS путь от {start_node} до {target_node}: {bfs_path}")
print(f"Итераций: {bfs_iterations}, Длина пути: {bfs_length}, Время: {bfs_time:.6f} сек")

print(f"\nDFS путь от {start_node} до {target_node}: {dfs_path}")
print(f"Итераций: {dfs_iterations}, Длина пути: {dfs_length}, Время: {dfs_time:.6f} сек")

print(f"\nДвунаправленный путь от {start_node} до {target_node}: {bidirectional_path}")
print(f"Итераций: {bidirectional_iterations}, Длина пути: {bidirectional_length}, Время: {bidirectional_time:.6f} сек")

# Сравнение сложности
print("\nСравнение сложности:")
print("- BFS: O(b^d) по времени и памяти (хранит все узлы текущего уровня)")
print("- DFS: O(b * d) по памяти, но O(b^d) по времени в худшем случае")
print("- Двунаправленный поиск: O(b^(d/2)) по времени и памяти (поиск с двух сторон)")

# Подсчет связанных вершин для n = 2 и n = 3
n2 = 2
n3 = 3

connected_n2 = graph.count_connected_nodes(target_node, n2)
connected_n3 = graph.count_connected_nodes(target_node, n3)

print(f"\nЧисло вершин, связанных с вершиной {target_node}:")
print(f"При n = {n2}: {connected_n2}")
print(f"При n = {n3}: {connected_n3}")