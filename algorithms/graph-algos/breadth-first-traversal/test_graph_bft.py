import unittest
import sys
import io
from graph_bft import Graph

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

    def test_bft(self):
        bft = [
            "1\n2\n3\n4\n5\n6\n7\n",
            "1\n2\n3\n4\n5\n7\n6\n",
            "1\n2\n3\n4\n6\n7\n5\n",
            "1\n2\n3\n4\n6\n5\n7\n",
            "1\n2\n3\n4\n7\n6\n5\n",
            "1\n2\n3\n4\n7\n5\n6\n",
            "1\n2\n4\n3\n5\n6\n7\n",
            "1\n2\n4\n3\n5\n7\n6\n",
            "1\n2\n4\n3\n6\n7\n5\n",
            "1\n2\n4\n3\n6\n5\n7\n",
            "1\n2\n4\n3\n7\n6\n5\n",
            "1\n2\n4\n3\n7\n5\n6\n"
        ]

        stdout_ = sys.stdout
        sys.stdout = io.StringIO()
        self.graph.bft(1)
        output = sys.stdout.getvalue()

        self.assertIn(output, bft)

        sys.stdout = stdout_  # Restore stdout


if __name__ == '__main__':
    unittest.main()
