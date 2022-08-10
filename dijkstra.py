"""Dijkstra Algorithm as a function"""

# Requirements for the function
import heapq
import sys

def backtrack(sequence, start, end):
    """Helper function to track the path taken to the end node.

    Args:
        sequence (dictionary): Containing 2-dictionary containing current and previously visited node.
        start (string): Starting node.
        end (string): Final node.

    Returns:
        list: Containing ordered list of nodes visited.
    """
    final = end
    track = []
    while start not in track:
        track.append(sequence[end])
        end = sequence[end]
    track.insert(0, final)
    return track

def remove_node(network, node):
    """Helper function to temporarily remove a node from the algorithm.

    Args:
        network (dictionary): Weighted graph represented in a dictionary format.
        node (string): The node to be removed.

    Returns:
        dictionary: Temporary weighted graph to be used in the algorim.
    """
    graph = network.copy()
    graph.pop(node)
    for x in graph:
        if node in graph[x]:
            graph[x].pop(node)
    return graph


def dijkstra(graph, start, end = None, skip = None): # Use get_graph() method to input into this function.
    """An algorithm that finds the shortest path between two nodes of a weighted graph. 
    In order to make sure the structure of the graph is correct, please use the Graph module to create a class.
    Use get_graph() method to use as a paramater for this function.

    Args:
        graph (dictionary): Derived from the Graph class containing nodes and edges.
        start (string): The starting node.
        end (string, optional): End node. Defaults to None.
        skip (string, optional): Node to be avoided. Defaults to None.

    Returns:
        If end node is specified: (dictionary): Containing nodes and the shortest distance to each node.
        If end node is not specified: (integer): The shortest distance to the end node from the start node. Also prints path taken.
    """    """"""
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
    elif distances[end] == "Unreachable":
        return print("Unreachable")
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

    dijkstra(graph, "Austin", "New York")
