# Queues 🚽  

## Queues
- FIFO: first-in, first-out - this means the oldest element, the item added first, is the first item to be removed

## Real World Example
- Bathroom queue/line 🚽🚶🏻‍♀️🚶🏽‍♂️ - the first person in line gets to go to the bathroom first
- Line at the DMV 

## Use cases
- Similar to LL and are typically used for breadth-first-searches for trees
- Might see this used to implement a cache
- What are real-world use-cases for a Queue data structure?

Queues are used anywhere in which you want to work with data First in First Out (FIFO). Server requests, without any prioritization, are handled this way. We'll also use it to conduct a breadth first traversal and breadth first search.



## Time Complexity
- Removing from the front is O(n)

## Queue Methods
3 primary methods: enqueue, dequeue, peek, and several helper methods: isEmpty, get Length

- `enqueue()`: add item to the BACK of the queue
- `dequeue()`: remove the first item from FRONT the queue
- `peek()`: return the item at the FRONT of the queue (but don't remove it)
- `isEmpty()`: check whether the queue is empty
- `length()`: returns the length of the queue



Should have the methods: enqueue, dequeue, and len.
enqueue should add an item to the back of the queue.
dequeue should remove and return an item from the front of the queue.
len returns the number of items in the queue.

![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)
