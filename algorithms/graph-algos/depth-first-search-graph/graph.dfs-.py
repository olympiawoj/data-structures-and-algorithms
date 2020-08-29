"""
Simple graph implementation



"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        DIRECTED means we are only adding this ONE way
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("Error: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("Error: Vertex does not exist")


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        create a stack
        push the starting vertex
        create a set to store visited vertices
        while stakc is not empty
            pop the first vertex
            check if its been visited
            if it hasnt been visited, mark as visited
                push all neighbors onto the stack

        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.


        This should be done using recursion. One tip for you is that when using your recursion, you don't need to implement your own stack because the recursive calls will be building their own stack

        Check if the node has been visited
        If NOT..
            Mark it as visited
            Call dft_recursive on each neighbor

        Biggest diff between graphs and trees is that graphs can be cyclic and loop back
        Trees always start from a root, but w/e you do a traversal you start from a root
        Big diff is dealing with cycles which is why we add visited note
        """

        # Check if the node is visited
        if visited is None:
            visited = set()
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
        if starting_vertex not in visited:
            # Mark starting vertex as visited
            visited.add(starting_vertex)
            # Print
            print(starting_vertex)
            # Call DFT_Recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        Create a queue
        Enqueue A PATH TO the starting vertex
        Create a set to store visited vertices
        While the queue is not empty..
            Dequeue the first PATH
            GRAB THE VERTEX FROM THE END OF THE PATH
            Check if it's been visited
            If it hasn't been visited..
                Mark it as visited
                Enqueue a PATH TO all it's neighbors
                    MAKE A COPY OF TH EPATH
                    ENQUEUE THE COPY 
        """
        q = Queue() 
        #enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        #create an empty set to store visited vertices
        visited = set()
        #while the queue is not empty
        while q.size() > 0:
            print('q', q.queue)
            #dequeue the first path
            path = q.dequeue()
            #grab the vertex from the end of the path
            v = path[-1]
            #check if it's the target
            if v == destination_vertex:
                #if so, return path
                return path 

            #check if its been visitied
            #if it has NOT been visited
            if v not in visited:
                #mark as visitied
                # print(v)
                visited.add(v)
                #enqueue a PATH to all its neighbors
                for neighbor in self.get_neighbors(v):
                    #make copy of path before adding, so no reference issues
                    copy = path.copy() 
                    copy.append(neighbor)
                    #enqueue the copy
                    q.enqueue(copy)

    ##breadth (queue) --> depth (stack)
    #depth NOt gteed to give shortesst path, breadth is
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        Create a stack
        PUSH A PATH TO the stacking vertex to the stack
        Create an empty set to store visited vertices
        While the stach is not empty..
            POP the first PATH
            GRAB THE VERTEX FROM THE END OF THE PATH
            Check if it's the target - if so, return the path
            Check if it's been visited
            If it hasn't been visited..
                Mark it as visited
                APPEND a PATH TO all it's neighbors on top of the stack
                    MAKE A COPY OF THE path before adding
                    append neighbor to copy
                    push to set 
        """
        # Create a stack
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push( [starting_vertex] )
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            print('here is v', v)
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # PUSH THE COPY
                    s.push(path_copy)


    #also need to store the path
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

            
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    #we should print this two times but bc we're storing our set is already filled up, not what we want
    #reason is bc for some reason,  Python will when it declares it ones, it'll keep a reference to that value for the entire time you have this function
    #do weird funky syntax - if we initialize visited as None and if its none then set it to set.  
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))