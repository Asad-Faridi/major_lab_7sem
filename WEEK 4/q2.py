import heapq
import math
cities = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['C', 'E'],
    'E': ['C', 'D']
}
def heuristic(city, goal):
    x1, y1 = cities[city]
    x2, y2 = cities[goal]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def best_first_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal), start, [start]))
    visited = set()
    while priority_queue:
        h, current, path = heapq.heappop(priority_queue)  # removes the city with the smallest priority
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor, path + [neighbor]) )
    return None

path = best_first_search('A', 'E')
print("Path:", path)