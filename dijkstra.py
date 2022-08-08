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
    visited = set() # Initialize empty visited set.
    unvisited = {node for node in graph} # Initializing unvisited set.
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
            visited.add(node)
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
        'Reykjavik': {'Berlin': 5},
        'Oslo': {'Rome': 5, 'Belgrade': 8},
        'Moscow': {'Berlin': 3},
        'London': {'Belgrade': 15},
        'Rome': {'Berlin': 4, 'Oslo': 5},
        'Berlin': {'Reykjavik': 5, 'Moscow': 3, 'Rome': 4},
        'Belgrade': {'Oslo': 8, 'London': 15},
        'Athens': {}}

    dijkstra(graph, "London")
