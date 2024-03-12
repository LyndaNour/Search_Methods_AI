from data import connections, coordinates
from dfs import *
from breadthFS import *
from best_first_search import *
from AstarSearch import *
from iddfs import *
import sys

def main():
    response ='Y'

    while True:
        print("Select a method you want to find a route from", 
              "\n1-Depth first search"
              "\n2-Breadth first search"
              "\n3-ID-DFS search"
              "\n4-Best first search"
              "\n5-A* search")
        
        while True:
            choice = int(input("Enter your choice (1-5): "))
            if choice >= 1 and choice <= 5:
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
            
        # Asking user to enter the start and target cities
        start_city = input("Enter the starting city: ")
        target_city = input("Enter the target city: ")
        
        if start_city in connections and target_city in connections:
            # Finding route based on user choice
            average_speed = float(input("Enter average speed (km/h): "))
            
            if choice == 1:
                find_route_dfs(connections, coordinates, start_city, target_city, average_speed)
            elif choice == 2:
                find_route_bfs(connections, coordinates, start_city, target_city, average_speed)
            elif choice == 3:
                find_route_id_dfs(connections, coordinates, start_city, target_city, average_speed)
            elif choice == 4:
                find_route_best_first(connections, coordinates, start_city, target_city, average_speed)
            elif choice == 5:
                find_route_a_star(connections, coordinates, start_city, target_city, average_speed)
        else:
            print("City not in the dictionary")

        response = input("Do you want to continue (Y/N)? ")
        response = response.upper()
        if response != 'Y':
            break

if __name__ == "__main__":
    main()
