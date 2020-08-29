
# Graphs 🕸

https://leetcode.com/discuss/general-discussion/655708/graph-problems-for-beginners-practice-problems-and-sample-solutions

## What are Graphs?
- A data structure that represents a collection of nodes and edges (which represent related data)
- They're _connections_ between  _nodes_
    - Nodes are called vertices, vertexes, and verts
    - Connections are called _edges_
- They're a non-linear data structure (as oppposed to a linked list, stack, or queue)

**A graph is a set of nodes/vertices and edges**
- Nodes can be connected by an  _edges_ or _connections_. Edges can connect nodes in ANY way they want. This connection represents a relationship or link between two nodes
- Can have many nodes, but it really only needfs one node to be a graph

### Graph Theory
- In math, graphs are just a way to represent a network. They're a collection of objects we order in a specific way that are all interconnected. 
- In math terms, we describe graphs as ordered pairs. In basic algebra, simplest ordered pair is (x, y)
- In graphs, it's G = (V, E). 
- However, in most graphs, we have more than 1 vertex and many edges.
    - So V is not 1 vertex, but the _set of vertices_ that make up the graph 
    - Similarly, E is not 1 edge but rather the _set of edges_ that make up the graph 
- In mathematics, **graphs** are defined as ordered pairs, with two parts: vertices and edges 
    - **Set of vertices** --> all of the nodes the graph has
    - **Set of edges** --> all of the links between those nodes
- In mathematics, the use of graph theory was to represent a network of interconnected objects
- When we think about how CS represents interconnected objects, those objects are the nodes and edges.


## Graphs vs. [Trees](../trees/README.md)  
- See trees here
- Trees flow in ONE direction, from the root node to child nodes. 
- Graphs have no formal starting point/ no root node. 

##
## Three Steps for solving ANY graph problem
1. Translate the problem into graph terminology
    - What are the nodes?
    - What are the edges?
    - Is it directed or undirected?
    - Is it cyclical or acyclical?
    - Is it weighted or unweighted?
2. Build your graph
3. Traverse your graph - using DFS or BFS

## Two Kinds of graphs
1. Directed - edges that function like one way streets (I follow you on Twitter, but you don't follow me)
2. Undirected - edges flow bi-directionally, like a two-way street (Your friends with me on Facebook, I'm freinds with you on Facebook.)

### Breadth vs Depth first search/traversals
- **Breadth First** goes ROW BY ROW to siblings before children
- **Depth First** goes DOWN VERTICALLY to all childs before siblings

### Definitions
- **Directed**: If edges are "one way" (have an arrow), the graph is directed, can only go from ONE node to another. (A) -> (B) means we can only travel from A to B, not from B to A. 
- **Undirected**: If there are no arrows, the edges are _bidirectional_. This means we can travel to both nodes in both directions. 
- **Cyclical vs. Acyclical**: If you can follow the edges and arrive at a node you've alrady visited, the graph is _cyclic_, otherwise it is _acyclic_ 
- **Weighted vs. Unweighted**: Graphs with values or _weights_ associated with the edges are _weighted_. Graphs with no values are _unweighted_. 
- **Dense vs. Sparse**: A graph where most vertices are connected to eachother is _dense). A graph with less connections is _sparse). 

## Graph Representations
Two most common ways are adjacency lists and an adjacency matrix
- **Adjacency Matrix**- a matrix representation of eactly WHICH nodes in the graph contain edges between them denoted by 0s (no edge between nodes) and 1s (an edge exists between the two nodes)
    - Matrix is represented as a 2D array or list of lists
    - Looking up, inserting, and removing an edge is O(1) constant time
    - Consumes O(V^2) amount of space
    - If a graph is sparse, the matrix will be mostly filled with 0s and take up a lot of space

```python
class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]
```

- **Adjacency List**- Each vertex is given an index in a list and has alll of it's neighboring vertices stored as an _array/linked list_, _adjacent_ to it. 

Note that this adjacency list doesn't actually use any lists. The `vertices` collection is a `dictionary` which lets us access each collection of edges in O(1) constant time while the edges are contained in a `set` which lets us check for the existence of edges in O(1) constant time.

```python
class Graph:
    def __init__(self):
        self.vertices = {
                          "A": {"B"},
                          "B": {"C", "D"},
                          "C": {"E"},
                          "D": {"F", "G"},
                          "E": {"C"},
                          "F": {"C"},
                          "G": {"A", "F"}
                        }
```


    - Retrieving a node's neighbors takes O(1) constant time (since we only need the node's index to get it's list of adjcaent neighbors)
    - To find a _specific_ edge (x, y), we need to find the vertex x's adjacency list which takes O(1) and look to see if y is in that list. Worst case, this takes O(d) time where d is the degree of vertex x. 
- **Edge List**



For the following:

```
V: Total number of vertices in the graph
E: Total number of edges in the graph
e: Average number of edges per vertex
```

### Space Complexity
* **Adjacency Matrix**: O(V ^ 2)
* **Adjacency List**: O(V + E)
- Takeaway: Adjacency lists are more space efficient for __sparse__ graphs while adjacency matrices become efficient for __dense__ graphs.
### Add Vertex
* **Adjacency Matrix**: O(V)
* **Adjacency List**: O(1)
- Takeaway: Adding vertices is very efficient in adjacency lists but very inefficient for adjacency matrices.
### Remove Vertex
* **Adjacency Matrix**: O(V ^ 2)
* **Adjacency List**: O(V)
- Takeaway: Removing vertices is inefficient in both adjacency matrices and lists but more inefficient in matrices.
### Add Edge
* **Adjacency Matrix**: O(1)
* **Adjacency List**: O(1)
- Takeaway: Adding edges to both adjacency lists and matrices is very efficient.
### Remove Edge
* **Adjacency Matrix**: O(1)
* **Adjacency List**: O(1)
- Takeaway: Removing edges from both adjacency lists and matrices is very efficient.
### Find Edge
* **Adjacency Matrix**: O(1)
* **Adjacency List**: O(1)
- Takeaway: Finding edges from both adjacency lists and matrices is very efficient.
### Get All Edges from Vertex
* **Adjacency Matrix**: O(V)
* **Adjacency List**: O(1)
- Takeaway: Fetching all edges is more efficient in an adjacency list than an adjacency matrix.


## Building a Graph Class
1. Create class Graph 
2. Add def__init__(self) method which represents a graph of vertices mapping lebsl to edges
3. def add_vertex method: t
4. Instantiate the graph first adding *nodes* then adding all *edges*

## DFS vs. BFS
- Breadth first uses **queues** which are like a bathroom line- FIFO (first in, first out)
    - Enqueue is adding to the back (append)
    - Dequeue is removing from front (pop at index 0)
- Depth first uses **stacks** and can do _recursion_. Stacks are like a stack of books- LIFO (last in, first out) or FILO (first in, last out)
    - Push adds to the back (append)
    - Pop removes from the back (LIFO)


## Helpful Links:

Introductary
- Base CS Video- Graph Theory: https://www.youtube.com/watch?v=uvcYL8ol4o8
- Base CS Podcast: Oily Graphs in Konisberg: https://www.codenewbie.org/basecs/19 
- Base CS Podcast: Let's get graphic: https://www.codenewbie.org/basecs/18
- Base CS Article- Introduction to Graph Theory: https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8
- Base CS Podcast- Seven Bridges and a triangle: https://www.codenewbie.org/basecs/20
- Base CS Article: Seven Bridges, One Giant Graph Problem: https://medium.com/basecs/k%C3%B6nigsberg-seven-small-bridges-one-giant-graph-problem-2275d1670a12
- Base CS Article: From Theory to Practice Representing Graphs: https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38


v1 and v2 is one single edge in the graph. It identifers the edge that connects these two nodes. 

A and B is one edge
B and A is one edge - same thing
This is bc of the fact that this is an undirected edge. Easy to go from one vertex to the other ane vice versa. 

https://www.youtube.com/user/purpongie/playlists
https://www.youtube.com/watch?v=pcKY4hjDrxk


Kevin Afable:lambda-tl:  11:02 AM
Bit minor but if you guys wanted better formatting for your terminal for dictionaries:
there's the pprint module with the pformat method that converts a dictionary into a more readable string with line breaks
import pprint
print(f"Friendships: \n{pprint.pformat(sg.friendships)}")



**Advantages of BFS:-**

1. Solution will definitely found out by BFS If there are some solution.2. BFS will never get trapped in blind alley , means unwanted nodes.3. If there are more than one solution then it will find solution with minimal steps.

**Disadvantages Of BFS :**

-1. Memory Constraints As it stores all the nodes of present level to go for next level.2. If solution is far away then it consumes time.

**Application Of BFS :**

-1.Finding Shortest Path.2.Checking graph with bipertiteness.3.Copying cheiney's Algorithm.

**Advantages Of DFS**

:-1. Memory requirement is Linear WRT Nodes.2. Less time and space complexity rather than BFS.3. Solution can be found out by without much more search.

**Disadvantage of DFS :-**

1. Not Guaranteed that it will give you solution.2. Cut-off depth is smaller so time complexity is more.3. Determination of depth until the search has proceeds.

**Applications of DFS:-**

1. Finding Connected components.2. Topological sorting.3. Finding Bridges of graph.