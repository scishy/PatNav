"""Dijkstra Algorithm as a function"""

import heapq
import sys

def dijkstra(graph, start):
    """Returns the shortest distances from the start node to all other nodes in a graph

    Args:
        graph (Dictionary): Output from graph class.
        start (String): The starting node
    """
    distances = {node: sys.maxsize for node in graph} # Set initial shortest distance to all nodes infinity.
    distances[start] = 0 # Setting starting node distance 0 from itself.
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
            """
            Find the shortest way of node and edge 
            1. Traversing distances from adjacent nodes on the target node
            2. Adds the distance from the current node to the adjacent node
            3. Change the distance of the node if the weight above the stored distance of the array is smaller
            4. Change if the weight is smaller than the distance stored in the array
            """
            current_distance, node = heapq.heappop(queue)
            if distances[node] < current_distance: 
                continue 

            for adjacency_node, distance in graph[node].items(): 
                weighted_distance = current_distance + distance
                if weighted_distance < distances[adjacency_node]:
                    distances[adjacency_node] = weighted_distance
                    heapq.heappush(queue, (weighted_distance, adjacency_node))
    for node in distances:
        if distances[node] > 10000:
            distances[node] = "Unreachable"
    return print(distances)

if __name__ == "__main__":
    graph = {
        'Houston': {'Boston': 5},
        'Nashville': {'Los Angeles': 5, 'Chicago': 8},
        'Toronto': {'Boston': 3},
        'Austin': {'Chicago': 15},
        'Los Angeles': {'Boston': 4, 'Nashville': 5},
        'Boston': {'Houston': 5, 'Toronto': 3, 'Los Angeles': 4},
        'Chicago': {'Nashville': 8, 'Austin': 15},
        'New York': {}}

    dijkstra(graph, "Austin")

    # Add end node functionality
    # Add skip node functionality
