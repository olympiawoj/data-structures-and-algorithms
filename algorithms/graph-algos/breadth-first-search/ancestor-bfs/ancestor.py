from util import Queue  # These may come in handy

#create a graph
class Graph:
    """
    Represent a graph of ancestor nodes, mapping parents relationship to children
    """
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        #add a vertext to the graph
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        #add relationship/edge to graph between ancestor/descendent DIRECTED means 1  way
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("Value Error: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("Error: Vertex does not exist")
        
def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        # graph.add_edge(pair[1], pair[0])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    #Enqueue a PATh to the starting vertex
    q.enqueue([starting_node])

    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        print('queue', q)
        #Dequeue the first path
        path = q.dequeue()
        #Grab the vertex from the end of the path
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            print('earliest ancestor', earliest_ancestor)
            max_path_len = len(path)
        # print('vertices', graph.vertices[v])
        #Enqueue a path to all it's neighbors
        for neighbor in graph.vertices[v]:
            print('neighbor', neighbor)
            #make a copy of the path
            path_copy = list(path)
            path_copy.append(neighbor)
            #enqueue the copy
            q.enqueue(path_copy)
    return earliest_ancestor



ancestors=[(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(ancestors, 1))
# #10


# print(earliest_ancestor(ancestors, 2))
# #-1 


print(earliest_ancestor(ancestors, 3))
#10