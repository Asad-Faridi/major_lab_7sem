from collections import deque
grid = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]
def find_path(grid):
    queue = deque()
    queue.append([(0, 0)])
    visited = set()
    visited.add((0, 0))
    directions = [(1, 0), (0, 1)]   
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == (3, 3):
            return path
        for direction in directions:
            row = current[0] + direction[0]
            col = current[1] + direction[1]
            if (0 <= row < len(grid) and
                0 <= col < len(grid[0]) and
                grid[row][col] == 0 and
                (row, col) not in visited):
                visited.add((row, col))
                new_path = list(path)
                new_path.append((row, col))
                queue.append(new_path)
    return None
path = find_path(grid)
print("Path:", path)