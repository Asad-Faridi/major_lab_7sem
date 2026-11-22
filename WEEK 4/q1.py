import heapq
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    open_list = []  # Priority queue
    heapq.heappush(open_list, (0, 0, start, [start]))   # (f_cost, g_cost, position, path)
    g_cost = {start: 0} # it stores The cheapest known cost to reach each cell from the start
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    while open_list:
        f, g, current, path = heapq.heappop(open_list) # This removes the cell with the smallest priority from the heap
        if current == goal:
            return path
        for dr, dc in directions:
            new_row = current[0] + dr
            new_col = current[1] + dc
            if new_row < 0 or new_row >= rows:
                continue
            if new_col < 0 or new_col >= cols:
                continue
            if grid[new_row][new_col] == 1:
                continue
            neighbor = (new_row, new_col)
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                h = manhattan_distance(neighbor, goal)   # h is estimated distance to goal
                f = new_g + h
                heapq.heappush(open_list,(f, new_g, neighbor, path + [neighbor]))
    return None

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal)
print("Shortest path:")
print(path)