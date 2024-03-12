from collections import deque
from data import connections
from data import coordinates
from dfs import haversine

def bfs(connections, start_node, target_node):
    # Queue for BFS
    queue = deque([(start_node, [start_node])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == target_node:
            return path

        visited.add(current_node)

        for neighbor in connections[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

def find_route_bfs(connections, coordinates, start, target, average_speed):
    route = bfs(connections, start, target)
    if route:
        total_distance = 0
        total_time = 0
        print(f"You will traverse {len(route)} cities")
        for i in range(len(route) - 1):
            current_city = route[i]
            next_city = route[i + 1]
            lat1, lon1 = coordinates[current_city]
            lat2, lon2 = coordinates[next_city]
            distance = haversine(lat1, lon1, lat2, lon2)
            total_distance += distance
            time = distance / average_speed  # Calculate time taken based on distance and average speed
            total_time += time
            print(f"Distance from {route[i]} to {route[i+1]} is: {distance:.2f} km")
            print(f"Time taken: {time:.2f} hours")
        print("Route found:", " -> ".join(route))
        print(f"Total distance: {total_distance:.2f} km")
        print(f"Total time: {total_time:.2f} hours")

    else:
        print("No route found from", start, "to", target)
