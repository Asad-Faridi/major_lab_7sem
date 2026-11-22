from collections import deque
start = (0, 0, 0, 0)
goal = (1, 1, 1, 1)

def is_valid(state):
    farmer, fox, chicken, grain = state
    # Fox and chicken cannot be together without farmer
    if fox == chicken and farmer != fox:
        return False
    # Chicken and grain cannot be together without farmer
    if chicken == grain and farmer != chicken:
        return False
    return True

def get_next_states(state):
    farmer, fox, chicken, grain = state
    # Farmer crosses alone
    new_state = (1 - farmer, fox, chicken, grain)
    if is_valid(new_state):
        yield new_state
    # Farmer takes fox
    if farmer == fox:
        new_state = (1 - farmer, 1 - fox, chicken, grain)
        if is_valid(new_state):
            yield new_state
    # Farmer takes chicken
    if farmer == chicken:
        new_state = (1 - farmer, fox, 1 - chicken, grain)
        if is_valid(new_state):
            yield new_state
    # Farmer takes grain
    if farmer == grain:
        new_state = (1 - farmer, fox, chicken, 1 - grain)
        if is_valid(new_state):
            yield new_state

def bfs():
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

solution = bfs()
for state in solution:
    print(state)