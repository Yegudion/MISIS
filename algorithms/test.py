import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")

        return dist

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        priority_queue = [(0, src)]
        
        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)

            if current_distance > dist[u]:
                continue

            for v, w in self.adj[u]:
                distance = current_distance + w
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(priority_queue, (distance, v))

        return dist

    def johnson(self):
        self.adj = [[] for _ in range(self.V)]
        for u, v, w in self.edges:
            self.adj[u].append((v, w))

        self.edges.append((self.V, v, 0) for v in range(self.V))
        
        try:
            h = self.bellman_ford(self.V)
        except ValueError as e:
            print(e)
            return

        for u in range(self.V):
            for i in range(len(self.adj[u])):
                v, w = self.adj[u][i]
                self.adj[u][i] = (v, w + h[u] - h[v])

        all_pairs_dist = []
        for u in range(self.V):
            dist_u = self.dijkstra(u)
            all_pairs_dist.append([dist_u[v] + h[v] - h[u] for v in range(self.V)])

        return all_pairs_dist

# Пример использования
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

distances = g.johnson()

for u in range(g.V):
    print(f"Расстояния от вершины {u}: {distances[u]}")