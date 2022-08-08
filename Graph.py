#Graph Class Module

# Steps to use
# First create an empty class using Graph()
# Then you can add a list of nodes using add_node_list(nodes) where nodes = ["London", "Paris",....]
# You can also add a single node using add_node(node) where node = "Bombay"
# Next add edges using add_edge(node1, node2, edge). Example: x.add_edge("London", "Paris", 5). 
# This will also create a reverse edge between the given nodes.
# You can get number of nodes using node_count method.
# You can get distance between 2 nodes using get_edge(node1, node2).
# You can remove a node from the graph using remove_node(node) method. This will also remove its edges.


class Graph:

    def __init__(self):
        """Initialize Class"""
        self.nodes = set() # Empty set, no duplicates
        self.graph = {} # Empty dictionary, no duplicates

    def __repr__(self):
        return str(self.graph)


    def add_node_list(self, nodes):
        """Add a list of nodes to the graph"""
        for node in nodes: 
            self.graph[node] = {} # Creates a key for each node and an empty dictionary as its value
            self.nodes.add(node) # Add each node to the node set
        return

    def add_node(self, node):
        """Add a single node to the graph"""
        self.graph[node] = {} # New key in the graph dictionary with empty dictionary as its value
        self.nodes.add(node) # Add new node to the node set
        return

    def add_edge(self, node1, node2, edge):
        """Create a weighted edge in the graph between node1 and node2"""
        # Making sure both nodes are in the graph
        if node1 not in self.nodes:
            print(node1 + " does not exist, please use add_node method.")
            return
        if node2 not in self.nodes:
            print(node2 + " does not exist, please use add_node method.")
            return
        # First we need to create a 1 way edge
        self.graph[node1][node2] = edge
        # Create a reverse edge
        self.graph[node2][node1] = edge
        return

    def node_count(self):
        """Returns the number of nodes in the graph class"""
        count = len(self.nodes)
        return count

    def get_nodes(self):
        """Returns list of nodes in the class"""
        return self.nodes

    def get_edge(self, node1, node2):
        """Returns the distance between two nodes if it exists"""
        # Making sure that the nodes exist
        if node1 not in self.nodes:
            print(node1 + " does not exist, please use add_node method.")
            return
        if node2 not in self.nodes:
            print(node2 + " does not exist, please use add_node method.")
            return
        if node2 not in self.graph[node1]:
            print("Edge does not exist, please use add_edge method.")
            return
        else:
            dist = self.graph[node1][node2]
            return dist

    def remove_node(self, node):
        """Removes the node from the graph class"""
        if node not in self.nodes:
            print("Node does not exist.")
            return
        else:
            self.nodes.remove(node)
            self.graph.pop(node)
            for x in self.nodes:
                if node in self.graph[x]:
                    self.graph[x].pop(node)
            print("Removed " + node)
            return

#Fix so that the output for x is iterable#

if __name__ == "__main__":
    x = Graph()
    nodes = ["Houston", "Boston", "Austin", "Las Vegas", "Los Angeles", "Chicago", "New York", "Nashville"]
    x.add_node_list(nodes)
    x.add_edge("Las Vegas", "Austin", 5)
    x.add_edge("Los Angeles", "Boston", 5)
    x.add_edge("Houston", "Chicago", 7)
    x.add_edge("New York", "Chicago", 15)
    x.add_edge("Nashville", "Austin", 12)
    x.add_edge("Boston", "New York", 3)
    x.add_edge("Houston", "Austin", 4)
    print(x)
    x.node_count()
    x.get_nodes()
    x.get_edge("Houston", "Austin")

