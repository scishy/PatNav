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


    


if __name__ == '__main__':
    unittest.main(verbosity=2)
