from queue import PriorityQueue
from data import connections
from data import coordinates
from dfs import haversine
import math
from dfs import dfs

def best_first_search(connections, start_node, target_node, heuristic):
    priority_queue = PriorityQueue()
    priority_queue.put((0, [start_node]))  # Priority queue to store nodes to be explored
    visited = set()

    while not priority_queue.empty():
        cost, path = priority_queue.get()
        current_node = path[-1]

        if current_node == target_node:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in connections[current_node]:
                if neighbor not in visited:
                    priority = heuristic[neighbor]
                    priority_queue.put((priority, path + [neighbor]))

    return None

def find_route_best_first(connections, coordinates, start, target, average_speed):
    heuristic = {}  # Heuristic information to estimate cost from each node to the target
    for city in connections:
        lat1, lon1 = coordinates[city]
        lat2, lon2 = coordinates[target]
        heuristic[city] = haversine(lat1, lon1, lat2, lon2)

    route = best_first_search(connections, start, target, heuristic)
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
