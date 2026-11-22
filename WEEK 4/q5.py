import math
import heapq
cities = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def mst_cost(remaining):
    if len(remaining) <= 1:
        return 0
    visited = {remaining[0]}
    total = 0
    while len(visited) < len(remaining):
        best_distance = float('inf')
        best_city = None
        for city1 in visited:
            for city2 in remaining:
                if city2 not in visited:
                    d = distance(city1, city2)
                    if d < best_distance:
                        best_distance = d
                        best_city = city2
        total += best_distance
        visited.add(best_city)
    return total

def tsp_a_star(start):
    cities_list = list(cities.keys())
    priority_queue = []
    heapq.heappush( priority_queue,(0, 0, start, (start,)))  # (f, g, current, path)
    best_cost = { (start, (start,)): 0} # This dictionary remembers the cheapest known cost for a particular state
    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)
        if len(path) == len(cities_list): # Check whether every city was visited
            total_cost = g + distance(current, start) # TSP requires us to return to the starting city
            return path + (start,), total_cost
        remaining = [city for city in cities_list if city not in path]  # list containing cities that haven't been visited yet        
        h = mst_cost(remaining)
        for next_city in remaining:
            new_g = g + distance(current, next_city)
            new_remaining = [ city for city in remaining if city != next_city ]          
            if new_remaining: # Are there still cities left after visiting next_city?
                new_h = mst_cost(new_remaining)
            else:
                new_h = 0
            f = new_g + new_h
            new_path = path + (next_city,)
            state = (next_city, new_path)
            if state not in best_cost or new_g < best_cost[state]:
                best_cost[state] = new_g
                heapq.heappush(priority_queue,(f, new_g, next_city, new_path))              
    return None, None

path, cost = tsp_a_star('A')
print("TSP Tour:")
print(path)
print("Total Distance:", round(cost, 2))