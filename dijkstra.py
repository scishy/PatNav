"""Dijkstra Algorithm as a function"""

import heapq
import sys

def backtrack(sequence, start, end):
    """Helper function to find the route taken"""
    final = end
    track = []
    while start not in track:
        track.append(sequence[end])
        end = sequence[end]
    track.insert(0, final)
    return track

def remove_node(network, node):
    """Helper function to remove node"""
    graph = network.copy()
    graph.pop(node)
    for x in graph:
        if node in graph[x]:
            graph[x].pop(node)
    return graph


def dijkstra(graph, start, end = None, skip = None): # Use get_graph() method to input into this function.
    """Returns the shortest distances from the start node to all other nodes in a graph. 

    Args:
        graph (Dictionary): Output from graph class. (Use the get_graph() method).
        start (String): The starting node
    """
    if skip is not None:
        graph = remove_node(graph, skip)

    distances = {node: sys.maxsize for node in graph} # Set initial shortest distance to all nodes infinity.
    distances[start] = 0 # Setting starting node distance 0 from itself.
    queue = []
    previous = {}
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
                    previous[adjacency_node] = node
                    heapq.heappush(queue, (weighted_distance, adjacency_node))
    for node in distances:
        if distances[node] > 10000:
            distances[node] = "Unreachable"

    
    
    if end == None:
        return print(distances)
    else:
        sequence = backtrack(previous, start, end)
        print(" <- ".join([str(x) for x in sequence]))
        return print(distances[end])

if __name__ == "__main__":
    graph = {
        'Houston': {'Boston': 5},
        'Nashville': {'Los Angeles': 5, 'Chicago': 8, 'Boston': 10},
        'Toronto': {'Boston': 3},
        'Austin': {'Chicago': 15},
        'Los Angeles': {'Boston': 4, 'Nashville': 5},
        'Boston': {'Houston': 5, 'Toronto': 3, 'Los Angeles': 4, 'Nashville': 10},
        'Chicago': {'Nashville': 8, 'Austin': 15},
        'New York': {}}

    dijkstra(graph, "Austin", "Boston", "Los Angeles")
