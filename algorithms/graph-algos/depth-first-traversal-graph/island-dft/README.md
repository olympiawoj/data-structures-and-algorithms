# Island Counter 

Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]
island_counter(islands) # returns 4

### What are connected components? 
- A _connected component_ of a graph is a subgraph where all vertices are reachable via edges in the subgraph.

### Usefulness of Connected Components
- There are a lot of theoretical uses of connected components that are beyond the scope of the course. But on the more practical front, here are some potential uses:
    * Look for people you might know in a social network.
    * Predict the spread of zombie apocalypse or other disease within social groups.
    * Determining which parts of a computer network are reachable from another.
    * Finding clusters of related information.

### Finding Connected Components
If you have a BFS or DFS, finding connected components is pretty
straightforward if you modify your search to return a list of verts
visited. (Also modify the search to not always color the verts white at
the start.)

```pseudocode
connected_components = [];

for v in graph.vertexes:
  v.color = white

for v in graph.vertexes:
  if v.color == white:
    component = bfs(v)
	connected_components.push(component);
```
### What are the inputs, outputs, and variables?
- **Inputs:** 2D binary array/matrix is our argument 
- **Output:**  Number of islands --> 4
- **Functions:**
    - `island_counter` is a function that counts the number of islands
- **Variables:** 

### Three Steps for solving ANY graph problem
1. Translate the problem into graph terminology
    - **What are the nodes?** Nodes are 1s
    - **What are the edges?** Where the 1s are connected - those are the edges
    - **Is it directed or undirected?** Undirected because we can see N and S are connected, E and W are connected
    - **Is it cyclical or acyclical?** Since it's undirected, it's definitely possible to have a cycle. Anytime a graph is undirected, it's probably cyclic 
    - **Is it weighted or unweighted?**   Unweighted because there are no values for edges
    - **Dense or Sparse, ratio of edges to modes?** 
    - **Connected Components?** Every node that you touch is a part of a connected component when you do a traversal 
directed  1s that are connected to N S E W
2. Build your graph 
    - We're counting the num of islands OR counting our number of connected components, how many graph components do we have in this graph?
    - 2D arrays and matrices are common, so understanding how to manipulate these are important. 
    - `islands` looks like an adjancency matrix but it is NOT an adjacency matrix. These are islands, not adjacencies. It's just a 2d representation of a graph. 
        - In adjacency matrix, 1s represent edges, nodes are rows and columns
        - In island matrix, 1s represent nodes, edges represented by connections between 1s 
3. Traverse your graph - using DFS or BFS
 
### island_counter 
**Goal:** Count how many groupings of 1 you have - each grouping counts as one island. The answer is 4. 
1. Create a visited matrix
2. Initialize an `island_count=0` 
3. Loop through the length of all nodes in the matrix - `for in in range(len(matrix)):` - this is going to be the _height_ of our matrix. Our matrix is 5 wide, 6 tall. 
4. If the node is not in visited vertices:
    - If we create a 1 that has not been visited
        - Mark it visited
        - Increment visited count
        - Traverse all connected nodes, marking as visited 
5. Return `island_count` at the end of all loops

### DFT Algorithm 
Goal: Do a DF traversal which returns a `visited` matrix 
1.  Create a graph you will traverse through
2.  Create a dft function which should accept a starting vertex
3.  Create a **stack** to help use keep track of vertices (or use a list/array)
    - Push the starting_vertex, a tuple `(row, col)` to the top of the stack
4. Use `while` to loop until the queue is empty. While the queue is NOT empty:
    - Pop a vertext from the stack
    - Use an `if` statement to check if that vertex has NOT been visited yet. If it hasn't:
        - `print(visited[row][col])`
        - Mark it as visited buy adding it to our set `visited[row][col] = True`
        - Get all of the vertex's neighbors using `self.get_neighbors(row, col, matrix)` and loop through every neighbor. 
            - Push every neighbor to the stack
6. **Return an updated visited matrix with all connected components marked as visited**


### get_neighbors Algorithm 
Goal: Return a list of neighboring 1 tupples in the from of [(row, col)]
1. Create an empty `neighbors=[]` array 
2. Check North: `if row > 0` and matrix[row-1][col]
3. Check South- `if row < len(matrix)-1` and matrix[row+1][col]
4. Check East- `if col < len(matrix[0])-1`and matrix[row][col +1] ==1
5. Check West- `if col > 0` and  matrix[row][col-1] == 1
- If any of the above are true, append to neighbors 
- **Gotchas** IndexError: Index out of bound if we dont check row/col lengths 
