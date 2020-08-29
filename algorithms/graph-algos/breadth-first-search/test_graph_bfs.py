import unittest
import sys
import io
from graph_bfs import Graph

class Test(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_vertex(4)
        self.graph.add_vertex(5)
        self.graph.add_vertex(6)
        self.graph.add_vertex(7)
        
        self.graph.add_edge(5, 3)
        self.graph.add_edge(6, 3)
        self.graph.add_edge(7, 1)
        self.graph.add_edge(4, 7)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(7, 6)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(4, 6)

    def test_vertices(self):
        vertices = {
          1: {2},
          2: {3, 4},
          3: {5},
          4: {6, 7}, 
          5: {3},
          6: {3},
          7: {1, 6}
        }
        self.assertDictEqual(self.graph.vertices, vertices)


    def test_bfs(self):
        bfs = [1, 2, 4, 6]
        self.assertListEqual(self.graph.bfs(1, 6), bfs)


if __name__ == '__main__':
    unittest.main()
