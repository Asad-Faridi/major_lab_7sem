import heapq
grid = [
    ['S', 1, 'X', 1, 1],
    [1, 1, 'X', 1, 'X'],
    [1, 1, 'B', 'B', 1],
    ['X', 'X', 'X', 'B', 1],
    [1, 1, 1, 1, 'T']
]
start = (0, 0)
goal = (4, 4)
directions = [(-1, 0), (1, 0),(0, -1),(0, 1)]
       
def get_cost(cell):
    if cell == 'B':
        return 0.5
    return 1

def heuristic(position, goal):
    distance = abs(position[0] - goal[0]) + abs(position[1] - goal[1])  # This calculates Manhattan distance
    return 0.5 * distance  # The cheapest walkable cell is a bonus cell with cost 0.5
                           # Therefore, the cheapest possible cost for distance remaining moves is approximately - 0.5 × distance

def a_star(grid, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue,(0, start, [start]))   
    cost_so_far = {  start: 0 }  # It stores the cheapest actual cost to reach each cell
    visited = set()
    while priority_queue:
        f, current, path = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path, f, visited
        for dr, dc in directions:
            new_row = current[0] + dr
            new_col = current[1] + dc
            if new_row < 0 or new_row >= len(grid):
                continue
            if new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[new_row][new_col] == 'X':
                continue
            neighbor = (new_row, new_col)
            movement_cost = get_cost(grid[new_row][new_col])
            new_g = cost_so_far[current] + movement_cost   # This calculates the actual cost so far
            if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_g
                h = heuristic(neighbor, goal)
                f = new_g + h
                heapq.heappush(priority_queue,(f, neighbor, path + [neighbor]))               
    return None, None, visited

path, total_cost, visited = a_star(grid, start, goal)
print("Best Path:")
print(path)
print("Total Cost:", total_cost)
print("Visited Nodes:", len(visited))