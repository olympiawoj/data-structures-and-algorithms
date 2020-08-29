# Depth First Traversal (DFT) - Graph

BFS - queues, neighBors first
DFS - stack, chilDren first

## Deoth-First Traversal
- An algorithm used to _traverse or move_ through a _graph_ to visit every single _node_
- Explore all possible paths to find the node you're looking for, traversing as far DOWN to CHILDREN as possible before 'backtracking' and visiting SIBLINGS
- Traversal is searching/visiting/checking each vertex in a graph
- Never revisits nodes
- Uses a QUEUE 

Traversal is searching/visiting/checking each vertex in a graph

### What is the difference between a Search and a Traversal?
- A search and a traversal are processed exactly the same.  The difference is:
- **In a search:** we stop when we find what we were looking for, or when all nodes have been visited without finding it 
- **In a traversal:** we always keep going until we've visited every node 

### Recursion
- A function which calls itself to solve a smaller version of the problem until hitting a base case

### Itertive vs. Recursive Approach
- Iterative uses a _stack_ to keep track of vertices visited
- Recursive doesn't use a stack because the recursive because recursive calls will be building their own call stack
- Note: You'll end up with a different order than the recursive solution, it'll still be depth first but it's a different order. 

### DFT Iterative Algorithm
1.  Create a graph you will traverse through
2.  Create a dft function which should accept a starting vertex
3.  Create a **stack** to help use keep track of vertices (or use a list/array)
    - Push the starting_vertex to the top of the stack
4. Create a **set** (or object) to store **visited** vertices 
    - Option: Create a **list** to store the end **result**, to be returned at the very end
5. Use `while` to loop until the stack is empty. While the stack is NOT empty:
    - Pop a vertext from the stack
    - Use an `if` statement to check if that vertex has NOT been visited yet. If it hasn't:
        - `print(v)`
        - Mark it as visited buy adding it to our set `visited.add(v)`
        - Get all of the vertex's neighbors using self.get_neighbors(v) and loop through every neighbor. 
            - Push every neighbor to the stack



## DFT Recursive Algorithm 
**Gotchas:** 
- One tip for you is that when using your recursion, you don't need to implement your own stack because the recursive calls will be building their own stack
- Also because we are using recursing and calling a function within itself, a new list it created _once_ when the function is defined and the same list is used in each successful call.  Hint: https://docs.python-guide.org/writing/gotchas/ 

1.  The function should accept a `starting_vertex` and a `visited=None` variable.
2.  Check `if visited is None`, if so create a **set** (or object) to store **visited** vertices 
    - Option: Create a **list** to store the end **result**, to be returned at the very end
3. Check `if starting vertex not in visited`. If not:
    - Mark the vertex as visited by adding it to our visited set
    - Print the starting_vertex
    - Get all the neighbors of the vertex and use a `while loop` to loop over every neighbor. For every neighbor:
        - Call our `dft_recursive` function recursively on our neighbor and visited set

