import unittest
from Graph import Graph
import dijkstra

# Testing the graph class first

class TestGraphClass(unittest.TestCase):

    def test_init(self):
        x = Graph()
        self.assertEqual(x.graph, {}) # should be empty

    def test_getgraph(self):
        x = Graph()
        x.add_node("London")
        x.add_node("Chicago")
        x.add_edge("London", "Chicago", 5)
        self.assertDictEqual(x.get_graph(), {'London': {'Chicago': 5}, 'Chicago': {'London': 5}})
    
    def test_addnodelist(self):
        x = Graph()
        nodes = ["London", "Chicago"]
        x.add_node_list(nodes)
        self.assertDictEqual(x.get_graph(), {'London': {}, 'Chicago': {}})

    def test_addnode(self):
        x = Graph()
        x.add_node("Chicago")
        self.assertSetEqual(x.nodes, {"Chicago"})

    def test_getedge1(self):
        x = Graph()
        x.add_node("Chicago")
        x.add_node("London")
        x.add_edge("Chicago", "London", 5)
        self.assertEqual(x.graph["Chicago"]["London"], 5)

    def test_nodecount(self):
        x = Graph()
        nodes = ["Houston", "Boston", "Austin", "Las Vegas", "Los Angeles", "Chicago", "New York", "Nashville"]
        x.add_node_list(nodes)
        self.assertEqual(x.node_count(), 8)

    def test_getnodes(self):
        x = Graph()
        x.add_node("A")
        x.add_node("B")
        self.assertSetEqual(x.get_nodes(), {"A", "B"})

    def test_getedge(self):
        x = Graph()
        x.add_node("A")
        x.add_node("B")
        x.add_edge("A", "B", 5)
        self.assertEqual(x.get_edge("A", "B"), 5)

    def test_removenode1(self):
        x = Graph()
        x.add_node("A")
        x.add_node("B")
        x.remove_node("B")
        self.assertSetEqual(x.get_nodes(), {"A"})

    def test_removenode2(self):
        x = Graph()
        x.add_node("A")
        x.add_node("B")
        x.add_node("C")
        x.add_node("D")
        x.add_edge("A", "B", 5)
        x.add_edge("B", "D", 7)
        x.add_edge("A", "C", 10)
        x.remove_node("B")
        self.assertDictEqual(x.get_graph(), {'A': {'C': 10}, 'C': {'A': 10}, 'D': {}})


# Testing the algorithm

class TestDijkstra(unittest.TestCase):

    def setUp(self):
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
        self.graph = x.graph

    def test_noend(self):
        self.assertDictEqual(dijkstra.dijkstra(self.graph, "Las Vegas"), {'Houston': 9, 'Boston': 9, 'Austin': 5, 'Las Vegas': 0, 'Los Angeles': 14, 'Chicago': 16, 'New York': 12, 'Nashville': 16, 'Baltimore': 'Unreachable'})
        
    def test_withend(self):
        self.assertEqual(dijkstra.dijkstra(self.graph, "Nashville", "New York"), 18)

    def test_withskip(self):
        self.assertEqual(dijkstra.dijkstra(self.graph, "Nashville", "Boston", "Austin"), 32)


if __name__ == '__main__':
    unittest.main(verbosity=2)
