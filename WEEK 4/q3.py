from collections import deque
import heapq
grid = [
    ['S', 0, 1, 0, 'G'],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (0, 4)
directions = [(-1, 0),(1, 0),(0, -1), (0, 1) ]

def bfs(grid, start, goal):
    queue = deque([(start, [start])])    # [start] is path
    visited = set()
    visited.add(start)
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path, visited
        for dr, dc in directions:
            new_row = current[0] + dr
            new_col = current[1] + dc
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 1:
                continue
            neighbor = (new_row, new_col)
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]) )                  
    return None, visited

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(grid, start, goal):
    priority_queue = []
    heapq.heappush( priority_queue,(0, 0, start, [start]))
    g_cost = {start: 0}
    visited = set()
    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path, visited
        for dr, dc in directions:
            new_row = current[0] + dr
            new_col = current[1] + dc
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 1:
                continue
            neighbor = (new_row, new_col)
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                h = manhattan_distance(neighbor, goal)
                f = new_g + h
                heapq.heappush(priority_queue, (f, new_g, neighbor, path + [neighbor]) )                  
    return None, visited

bfs_path, bfs_visited = bfs(grid, start, goal)
astar_path, astar_visited = a_star(grid, start, goal)
print("BFS Path:")
print(bfs_path)
print("BFS Steps:", len(bfs_path) - 1)
print("BFS Visited Nodes:", len(bfs_visited))
print("\nA* Path:")
print(astar_path)
print("A* Steps:", len(astar_path) - 1)
print("A* Visited Nodes:", len(astar_visited))