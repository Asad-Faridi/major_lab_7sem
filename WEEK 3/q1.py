from collections import deque
def solve_maze(maze, start, end):
    queue = deque([[start]])
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == end:
            return path
        for d in directions:
            next_row_col = (current[0] + d[0], current[1] + d[1])
            r, c = next_row_col
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0 and next_row_col not in visited:
                visited.add(next_row_col)
                new_path = list(path)     # Because we want to create a new path without changing the original path
                new_path.append(next_row_col)
                queue.append(new_path)               
    return None 
my_maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]
start_position = (0, 0) 
end_position = (3, 3)   
path = solve_maze(my_maze, start_position, end_position)
print("Winning Path:", path)