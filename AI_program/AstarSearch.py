from queue import PriorityQueue
from data import connections
from data import coordinates
from dfs import haversine
import math
from queue import PriorityQueue

def astar_search(connections, coordinates, start_node, target_node, average_speed):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_node))  # Priority queue to store nodes to be explored
    came_from = {}
    cost_so_far = {start_node: 0}  # Cost from start to current node
    heuristic = {}  # Heuristic information to estimate cost from each node to the target

    # Calculate heuristic for each city
    for city in connections:
        lat1, lon1 = coordinates[city]
        lat2, lon2 = coordinates[target_node]
        heuristic[city] = haversine(lat1, lon1, lat2, lon2)

    while not priority_queue.empty():
        _, current_node = priority_queue.get()

        if current_node == target_node:
            break

        for neighbor in connections[current_node]:
            new_cost = cost_so_far[current_node] + haversine(*coordinates[current_node], *coordinates[neighbor]) / average_speed
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                priority_queue.put((priority, neighbor))
                came_from[neighbor] = current_node

    path = []
    current = target_node
    while current != start_node:
        path.append(current)
        current = came_from[current]
    path.append(start_node)
    path.reverse()

    return path

def find_route_a_star(connections, coordinates, start, target, average_speed):
    route = astar_search(connections, coordinates, start, target, average_speed)
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
