from data import connections
from data import coordinates
from dfs import haversine
import math
from dfs import dfs

def iddfs(connections, current_node, target_node, max_depth, current_depth=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if current_node == target_node:
        return path

    if current_depth < max_depth:
        visited.add(current_node)
        path.append(current_node)  

        for neighbor in connections[current_node]:
            if neighbor not in visited:
                result = iddfs(connections, neighbor, target_node, max_depth, current_depth + 1, visited, path)
                if result:
                    return result

        path.pop()
        return None

def find_route_id_dfs(connections, coordinates, start, target, average_speed):
    max_depth = len(connections)  # Maximum depth to explore
    route = iddfs(connections, start, target, max_depth)
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
