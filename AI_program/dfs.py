from data import connections
from data import coordinates
import math

def dfs(connections, current_node,target_node, visited=None, path=None):
    if visited is None:
        visited = set()
        if path is None:
            path = []
    visited.add(current_node)
    path.append(current_node)  # Print the current node

    if current_node == target_node:
        return path  # Return the path if the target node is reached

    for neighbor in connections[current_node]:
        if neighbor not in visited:
            result = dfs(connections, neighbor,target_node, visited, path)
            if result:
                return result
            
    path.pop()  # Remove current node from the path if no path found
    return None  # Return None if no path found

def haversine(lat1, lon1, lat2, lon2):
  
   # Calculate the great-circle distance between two points 
    #on the Earth's surface using the Haversine formula.

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371  # Radius of the Earth in kilometers
    distance = r * c
    return distance

def find_route_dfs(connections, coordinates, start, target, average_speed):
    route = dfs(connections, start, target)
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
            time = distance / average_speed 
            total_time += time
            print(f"Distance from {route[i]} to {route[i+1]} is: {distance:.2f} km")
        print("Route found:", " -> ".join(route))
        print(f"Total distance: {total_distance:.2f} km")
        print(f"Total time: {total_time:.2f} hours")

    else:
        print("No route found from", start, "to", target)

