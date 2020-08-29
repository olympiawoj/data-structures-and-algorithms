# Breadth First Search 🔍

## Breadth First Search
- Searching algorithm that visits every _sibling node_ horizontally before moving down to visit _child nodes_

## Data Structures to use
- Uses a _queue_ which is FIFO
    - enqeue 
    - dequeue
- Can use an _array_ for FIFO
    - push to add things in to the end of an rray
    - shift to remove from beginning

## Steps to BFS Iterative
- Create a queue (this can be an array) and a variable to store the values of nodes visited (FIFO structure)
- Place the root node in the queue
- Loop as long as there is anything in the queue
    - **Denqueue a node from the queue** and push the value of the node into the variable that stores the node
    - **If there is a left property** on the node dequeued - add it to the queue
    - **If there is a right property** on the node dequeued - add it to the queue
- Return the variable that stores the values

## Steps to BFS Recursive