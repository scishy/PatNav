
# PatNav

PatNav is a weighted network navigation package. 
It allows for the creation of weighted networks as well as 
functions to navigate through the network when given various
parameters.


## Organization

**graph.py**: This module is used for creating and editing
a weighted network. This module implements a class called
Graph. 

**dijkstra.py**: This module contains a dijkstra function
and helper functions used to navigate the network created in the
graph class.

**test.py**: This module performs unit testing on the other two modules.


## Features

- Create weighted networks.
- Add nodes one at a time or as a list.
- Remove nodes.
- Add distances (weights) between two nodes.
- Get node counts and lists.
- Visualize the weighted network.
- Find the shortest path from start node to all other nodes.
- Find the shortest path from the start node to an end node.
- Find the shortest path from a start node to end node while avoiding a certain node.


## Classes, Functions and Parameters

1. **Graph (class)**: Implements a weighted network.
    - get_graph(): Returns the network as a dictionary.
    - add_node(node): Adds the node to the network.
    - add_node_list([node]): Adds a list of nodes to the network
    - add_edge(node1, node2, edge): Adds an edge between node1 and node2 with weighted
    - node_count(): Returns the total number of nodes in the network.
    - get_nodes(): Returns a list of nodes in the network.
    - get_edge(node1, node2): Returns the edge (weight) between node1 and node2.
    - remove_node(node): Removes the node and its edges from the network.
    - visualize(seed = 5): Displays a visualization of the network. The user can change configuration of the visualization by changing the seed.

2. **dijkstra(graph, start, end = None, skip = None)**: Returns the shortest path from the starting node.
    - graph: Output of the graph class. Retreived using get_graph() method.
    - start: The starting node. 
    - end: Optional end node. If provided, function will print a path sequence and a total length.
    - skip: The node to be ignored. Function will return a path without this node.
    
## Usage/Examples
As a Jupyter Notebook: https://drive.google.com/file/d/13temd0E0EgE9kScaBXNQUmiKgK7BYfRe/view?usp=sharing

```Python
from PatNav import dijkstra as dj
from PatNav import graph as g

x = g.Graph()
nodes = ["Houston", "Boston", "Austin", "Las Vegas", "Los Angeles", "Chicago", "New York", "Nashville"]
x.add_node_list(nodes)
x.add_edge("Las Vegas", "Austin", 5)
x.add_edge("Los Angeles", "Boston", 5)
x.add_edge("Houston", "Chicago", 7)
x.add_edge("New York", "Chicago", 15)
x.add_edge("Nashville", "Austin", 12)
x.add_edge("Boston", "New York", 3)
x.add_edge("Houston", "Austin", 4)
x.add_edge("Nashville", "Houston", 7)
x.add_edge("Boston", "Austin", 4)

x.get_nodes() #{'Austin', 'Nashville', 'Houston', 'Boston', 'Chicago', 'Los Angeles', 'Las Vegas', 'New York'}
x.node_count() #8
x.get_graph()
                        #{'Houston': {'Chicago': 7, 'Austin': 4, 'Nashville': 7}, 
                        #'Boston': {'Los Angeles': 5, 'New York': 3, 'Austin': 4}, 
                        #'Austin': {'Las Vegas': 5, 'Nashville': 12, 'Houston': 4, 'Boston': 4}, 
                        #'Las Vegas': {'Austin': 5}, 'Los Angeles': {'Boston': 5}, 
                        #'Chicago': {'Houston': 7, 'New York': 15}, 'New York': {'Chicago': 15, 'Boston': 3}, 
                        #'Nashville': {'Austin': 12, 'Houston': 7}}

x.get_edge("Nashville", "Austin") #12
x.remove_node("Boston") # Removed Boston
x.get_graph()
                        #{'Houston': {'Chicago': 7, 'Austin': 4, 'Nashville': 7}, 
                        # 'Austin': {'Las Vegas': 5, 'Nashville': 12, 'Houston': 4}, 
                        # 'Las Vegas': {'Austin': 5}, 'Los Angeles': {}, 
                        # 'Chicago': {'Houston': 7, 'New York': 15}, 
                        # 'New York': {'Chicago': 15}, 
                        # 'Nashville': {'Austin': 12, 'Houston': 7}}

x.add_node("Boston")
x.add_edge("Boston", "Austin", 4)
x.add_edge("Boston", "New York", 3)
x.add_edge("Los Angeles", "Boston", 5)
#x.visualize() # See screenshots

dj.dijkstra(x.get_graph(), "Las Vegas")
                        #{'Houston': 9, 'Austin': 5, 'Las Vegas': 0, 'Los Angeles': 14, 
                        # 'Chicago': 16, 'New York': 12, 'Nashville': 16, 'Boston': 9}

dj.dijkstra(x.get_graph(), "Las Vegas", "New York")     # New York <- Boston <- Austin <- Las Vegas
                                                        # 12
                                                        
dj.dijkstra(x.get_graph(), "Las Vegas", "New York", skip = "Boston")        # New York <- Chicago <- Houston <- Austin <- Las Vegas 
                                                                            # 31

dj.dijkstra(x.get_graph(), "Las Vegas", "New York", skip = "Austin") # Unreachable
