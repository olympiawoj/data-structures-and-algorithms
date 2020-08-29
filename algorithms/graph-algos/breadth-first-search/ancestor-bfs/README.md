# Earliest Ancestor

This is a take-home coding challenge from a top tech company. The spec is providied verbatim.


### Problem

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

```
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
```

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

#### What are the inputs, outputs, and variables?
- **Inputs:** List of data describing a graph of relationships between parent and children, formatted as (parent, child) pairs
    - Each individual is assigned a *UNIQUE* integer indentifer
    - Arguments: ancestors (list of ancestors) and starting_node (where we start our search from)
- **Output:** 
    - Return the *id* of the ancestor furthest from the input individual 
    - If there's a tie, return the one with the lowest numer ic id
    - If a child has no parent, return -1
- **Variables**: we'll need a variable to track the `earliest_ancestor` AND a variable to track the `max_path_len` since output is the id of the _furthest ancestor_
    - Initialize earliest ancestor to -1 because we should assume no ancestor until we find one
- Because we are tring to find a particular ancestor node, this means we are doing a **search** and need to track a path to the earliest ancestor and then return the id of that anciestor
- **Control Flow** - Every time we loop, we store the path and then check if that path is longer to or equal to our `max_path_len` AND the `v` is smaller OR if the path is longer than `max_path_len`

### Gotchas
- Because we're looking for our ancestor, we need to build edges in REVERSE `graph.add_edge(pair[1], pair[0])`

### BFS vs DFS - when to choose what? Understand
- Since we need to find the furthest ancestor and return it, we know we're going to perform a _graph search_
- BFS vs DFS? If you know the solution is not far from the tree, BFS. If the tree is very deeep and solutions are rare, DFS may take a very long time while BFS may be faster. If solutions are deep in the tree, a BFS could be impractical. 
- BFS used to construct shortest path problems, shortest # of moves, etc
- DFS - topological sorting i.e. resolving dependencies

#### Three Steps for solving ANY graph problem
1. Translate the problem into graph terminology
    - What are the nodes? The nodes are parents and their children 
    - What are the edges? Edges are the relationships between parents and children
    - Is it directed or undirected? Undirected because there are no arrows
    - Is it cyclical or acyclical? Acyclic - you cannot go traverse through it in a cycle
    - Is it weighted or unweighted? Unweighted - no values for the edges
2. Build your graph 
3. Traverse your graph - using DFS or BFS


### BFS Algorithm 
Goal = traverse through a graph BFT until we find a node we're looking for, returning a path to the node we find

1. **Build the graph** of ancestors and parent/children relationships with a Graph class. Methods needed:
    - init
    - add_vertex
    - add_eddge
    - get_neighbors
    - earliest-ancestors: 
        - Initialize our graph
        - Loop over every pair in our ancestor list adding each vertex
        - Loop through every pair again to add the edges *after* all of the nodes have been added 

**earliest_ancestors**
1. **Create a Queue** (or use an array)
2. **Enqueue the starting index** (starting with a node)  
    - Enqueue means add to the add to the back/end of queue
3.  Declare our two variables `max_path_len = 1` and `earliest_ancestor = -1` 
4. Use `while` to loop until the queue is empty. While the queue is not empty:
    - Dequeue/remove the first PATH from the queue
    - Grab the vertex from the end of the path `v = path[-1]`
    - Check if the `len(path)` is longer or equal to `max_path_len` AND the vaue is smaller than `earliest_ancestor` OR if the `len(path)` is greater than `max_path_en`
        - If true, we know the vertex is a candidate for our solution so we set earliest_ancestor equal to our `v` vertex and print it 
        - Set our `max_path_len = len(path)` because we know this is our longest path to our candidate so far
        - Next, loop through all of that vertex's _neighbors_ . graph.vertices gets all the vertices in the graph so graph.vertces[v] gets 



    - Check if that vertex has NOT been visited by seeing if its in our `visited` set
    - If it hasn't been visited, add it to the visited set `visited.add(v)` a
    - Check if this vertex is our target/destination vertex. 
    - If it is, return the path
    - Get all neighbors and loop over every neighbor. For every neighbor:
        - Make a copy of the path `path_copy = path.copy()`
        - Append the neighbor to the path i.e. the next node you visited `path.append(neighbor)`
        - Enqueue the copy / add to the queue so the loop runs again 
4. You will eventually finish looping either because 1) the vertex matched the target and earliest_ancestor was returned OR 2) there is no earliest ancestor and -1 was returned 