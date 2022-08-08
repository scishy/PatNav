"""A function to create a graphical representation of the graph class"""

#Graph visualization module
#requires networkx and matplotlib.pyplot to create visual representation of graph structure

#CITATION: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html

#Directions: first create object using graph module. Then use visualize(object.getgraph()) to plot the chart

import matplotlib.pyplot as plt
import networkx as nx


def visualize(graph):
    G = nx.Graph()
    for node1 in graph:
        for node2 in graph[node1]:
            G.add_edge(node1, node2, weight = graph[node1][node2])

    # Position
    pos = nx.spring_layout(G, seed=5)

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
