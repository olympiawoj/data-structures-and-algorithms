# Breadth First Traversal (BFT) - Graph

BFS - queues, neighBors first
DFS - stack, chilDren first

## Breadth-First Traversal
- An algorithm used to _traverse or move_ through a _graph_ to visit every single _node_
- Explore all possible paths to find the node you're looking for, traversing ACROSS siblings before traversing down
- Never revisits nodes
- Uses a QUEUE 

### Queues follow FIFO
- First in first out
- Enqueue, means add to the back/end of list
- Dequeue, means remove from the top 



### BFT Algorithm 
Goal = traverse through a graph BFT and visit/print out *every node*

1. Create a queue (or use an array)
2. Enqueue a PATH to the starting vertex - the path is an array
    - Enqueue means add to the add to the back/end of queue
3. Create a [set](../data-structures/basics/set) to store visited vertices
4. Use `while` to loop until the queue is empty. While the queue is not empty:
    - Dequeue/remove the first vertex from the queue
    - Check if that vertex has NOT been visited by seeing if its in our `visited` set
    - If it hasn't been visited, add it to the `visited` set and PRINT IT
    - Get all neighbors and execute a for loop to enqueue every neighbor
5. Once you have finished looping, return an array of visited nodes 