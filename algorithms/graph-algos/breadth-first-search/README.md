# Breadth First Search (BFS) - Graph

BFS - queues, neighbors first
DFS - stack, chilDren first

## Breadth-First Search
- An algorithm used to _traverse or move_ through a _graph_ and find a solution. We stop when we find what we're looking for OR when all nodes have been visited without finding it. 
- Explore all possible paths to find the node you're looking for, traversing ACROSS siblings before traversing down
- Never revisits nodes
- Like a **B**athroom, it uses a QUEUE 


### What is the difference between Breadth First and Depth First?
- **Depth First:** Pick one path at each branch and keep going DOWN/forward until we hit a dead end, then  backtrack and take the first branch we find. 
- **Breadth First:** We go by layers, one row deeper each time.  This means that we jump around a bit.



### Queues follow FIFO
- First in first out
- Enqueue, means add to the back/end of list
- Dequeue, means remove from the top 

### Uses
- Good for when solutoin is NOT far from the route - 'shortest path' problem
- Find a route or path from A to B location 
- Social networking - suggest a number of friends you might know
- Networking applications 

### BFS Algorithm 
Goal = traverse through a graph BFT until we find a node we're looking for, returning a path to the node we find

<!-- **The Algorithm**

1. Begin at the starting vertex (s)- on a tree, this would be the root of out tree, on an undirected graph we'd have a starting vertex labeled
2. Explore vertex
    - While +1 unscheduled vertices adjacent to current vertex
        - Schedule adjacent vertex to be explored using a [**QUEUE**]
3. Mark vertex as explored (remove from queue)

- We can use BFS to traverse a graph, **starting at levels closest to the root and finishing at those furthest away**
- Good if you are solving a derivative of the **"shortest path" problem** or other scenarios where you know the **solution is NOT far from the root.** -->
<!-- **Why path instead of the node itself  —>** 

- Bc we need to store the path
- What about the visited set? Now, visited is NOT going to be the path -->


1. Create a queue (or use an array)
2. Enqueue a path starting index (starting with a node)  
    - Enqueue means add to the add to the back/end of queue
3. Create a [set](../data-structures/basics/set) to store visited vertices
4. Use `while` to loop until the queue is empty. While the queue is not empty:
    - Dequeue/remove the first PATH from the queue
    - Grab the vertex from the end of the path `v=path[-1]`
    - Check if that vertex has NOT been visited by seeing if its in our `visited` set
    - If it hasn't been visited, add it to the visited set `visited.add(v)` a
    - Check if this vertex is our target/destination vertex. 
    - If it is, return the path
    - Get all neighbors and loop over every neighbor. For every neighbor:
        - Make a copy of the path `path_copy = path.copy()`
        - Append the neighbor to the path i.e. the next node you visited `path.append(neighbor)`
        - Enqueue the copy / add to the queue so the loop runs again 
5. You will eventually finish looping either because 1) the vertex matched the target and returned the path OR 2) the vertex is not in the graph



Traversal is searching/visiting/checking each vertex in a graph





# Breadth First Search (BFS)

## Objective

* Learn about one of the more famous graph algorithms
* Learn uses of BFS

## Overview

When searching a graph, one of the approaches is called _breadth first
search_. This explores the graph outward in rings of ever increasing
distance from the starting vertex. 

The algorithm never attempts to explore a vert that it either has
explored or is exploring.

For example, when starting from the upper left, the numbers on this
graph show a vertex visitation order in a BFS:

![BFS visit order](img/bfs-visit-order.png)

The bold lines show with edges were followed. (The thin edges were not
followed since their destination nodes had already been visited.)

(Of course, the exact order will vary depending on which branches get
taken first and which vertex is the starting vertex.)

## Uses of BFS

* Pathfinding, Routing 
* Find neighbor nodes in a P2P network like Bittorrent 
* Web crawlers 
* Finding people n connections away on a social site 
* Find neighboring locations on graph 
* Broadcasting in a network 
* Cycle detection in a graph 
* Finding [Connected Components](https://en.wikipedia.org/wiki/Connected_component_(graph_theory))
* Solving a number of theoretical graph problems 

## Coloring Vertexes

As the graph is explored, it's useful to color verts as you arrive at
them and as you leave them behind as "already searched".

Commonly, unvisited verts are white, verts whose neighbors are being
explored are gray, and verts with no unexplored neighbors are black.


## Keeping Track of What We Need to Explore

In BFS, it's useful to track which nodes we need to follow up on. For
example, in the diagram above, when we get to node 2, we need to explore
node 3 and 4 in the future, in order.

We can track that by adding neighbors to a _queue_, and then exploring
the verts in the queue.


## Pseudocode for BFS

```pseudocode
BFS(graph, startVert):
  for v of graph.vertexes:
    v.color = white

  startVert.color = gray
  queue.enqueue(startVert)

  while !queue.isEmpty():
    u = queue[0]  // Peek at head of queue, but do not dequeue!

    for v of u.neighbors:
      if v.color == white:
        v.color = gray
        queue.enqueue(v)
    
    queue.dequeue()
    u.color = black
```

## Exercises

* Build a random graph and show a vertex visitation order for BFS.

* One more for good measure.
