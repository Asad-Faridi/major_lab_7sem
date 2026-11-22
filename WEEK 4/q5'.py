import heapq
grid = [
    ['S', 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 'G1', 0, 0],
    [0, 1, 'G2', 1, 0],
    [0, 0, 0, 0, 'G3']
]
start = (0, 0)
goals = {
    (2, 2),
    (3, 2),
    (4, 4)
}
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(position, remaining_goals):
    if not remaining_goals:
        return 0
    return min(
        manhattan(position, goal)
        for goal in remaining_goals
    )

def multi_goal_a_star(grid, start, goals):
    priority_queue = []
    initial_state = (start, frozenset())
    heapq.heappush(
        priority_queue,
        (0, 0, start, frozenset(), [start])
    )
    best_cost = {
        initial_state: 0
    }
    while priority_queue:
        f, g, current, visited_goals, path = heapq.heappop(
            priority_queue
        )
        if visited_goals == frozenset(goals):
            return path, g
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
            new_visited_goals = visited_goals
            if neighbor in goals:
                new_visited_goals = visited_goals | {neighbor}
            new_g = g + 1
            state = (neighbor, frozenset(new_visited_goals))
            if state not in best_cost or new_g < best_cost[state]:
                best_cost[state] = new_g
                remaining_goals = goals - new_visited_goals
                h = heuristic(
                    neighbor,
                    remaining_goals
                )
                f = new_g + h
                heapq.heappush(
                    priority_queue,
                    (
                        f,
                        new_g,
                        neighbor,
                        frozenset(new_visited_goals),
                        path + [neighbor]
                    )
                )
    return None, None

path, cost = multi_goal_a_star(
    grid,
    start,
    goals
)
print("Multi-Goal Path:")
print(path)
print("Total Steps:", cost)