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
# You can create a visualization of the graph at any point using the visualize() method. Eg: x.visualize()

# Needed for the visualize method
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    """This class provides an implementation of a weighted network. 
    It stores nodes and its edges and provides a method to visualize it.
    """

    def __init__(self):
        """Initializes the class"""
        self.nodes = set() # Empty set, no duplicates
        self.graph = {} # Empty dictionary, no duplicates

    def __repr__(self):
        """String representation.

        Returns:
            String: Printed Graph.
        """
        return str(self.graph) # self.graph converted into a string

    def get_graph(self):
        """Returns the graph usable with an external function.

        Returns:
            Dictionary: Containing nodes and edges.
        """
        return self.graph # returns the graph as a parameter

    def add_node_list(self, nodes):
        """Adds a list of nodes to the graph.

        Args:
            nodes (list): Containing node labels as strings.
        """
        for node in nodes: 
            self.graph[node] = {} # Creates a key for each node and an empty dictionary as its value
            self.nodes.add(node) # Add each node to the node set
        return

    def add_node(self, node):
        """Adds a single node to the graph.

        Args:
            node (string): Node to be added to the graph class.
        """
        self.graph[node] = {} # New key in the graph dictionary with empty dictionary as its value
        self.nodes.add(node) # Add new node to the node set
        return

    def add_edge(self, node1, node2, edge):
        """Adds an edge between node1 and node2 in the graph class.

        Args:
            node1 (string): From node.
            node2 (string): To node.
            edge (int): Distance or weight between the nodes.
        """
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
        """Returns the number of nodes in the graph class.

        Returns:
            int: Number of nodes in the graph class.
        """
        count = len(self.nodes)
        return count #integer

    def get_nodes(self):
        """Returns a list of nodes in the graph class.

        Returns:
            list: Containing the node labels.
        """
        return self.nodes #list

    def get_edge(self, node1, node2):
        """Returns the edge between two given nodes.

        Args:
            node1 (string): First node.
            node2 (string): Second node.

        Returns:
            int: The distance or weight between two nodes.
        """
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
            return dist #integer

    def remove_node(self, node):
        """Removes a node from the graph class and deletes corresponding edges.

        Args:
            node (string): Node to be removed.
        """
        # Making sure that the node exists
        if node not in self.nodes:
            print("Node does not exist.")
            return
        else:
            #First removing from the node list
            self.nodes.remove(node)
            #Removing the node and its connections
            self.graph.pop(node)
            #Removing any other connections to this node in the graph
            for x in self.nodes:
                if node in self.graph[x]:
                    self.graph[x].pop(node)
            print("Removed " + node)
            return

    def visualize(self, seed = 5):
        """Creates a visual representation of the graph class.

        Args:
            seed (int, optional): Used to change the orientation of the nodes in the graph. Defaults to 5.
        """
        # Citation: the creation of this method uses this documentation as reference.
        # https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html

        # Creating an empty networkx class
        G = nx.Graph()

        # Unpacking the graph to add to the networkx clas
        for node1 in self.graph:
            if self.graph[node1] == {}:
                G.add_node(node1)
            for node2 in self.graph[node1]:
                G.add_edge(node1, node2, weight = self.graph[node1][node2])

        # Position
        pos = nx.spring_layout(G, seed = seed)

        #Edges
        edge_list = [(u, v) for (u, v, d) in G.edges(data=True)]

        #Draw Nodes
        nx.draw_networkx_nodes(G, pos, node_size=500)

        #Draw edges
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, width=5, edge_color = (234/255.0,182/255.0,118/255.0))

        #Draw node labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

        #Edge Labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        #Display
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

        return

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
    x.add_edge("Nashville", "Houston", 7)
    x.add_edge("Boston", "Austin", 4)
    x.add_node("Baltimore")
    x.visualize()
    import dijkstra
    dijkstra.dijkstra(x.get_graph(), "Las Vegas", "Los Angeles", "Austin")

