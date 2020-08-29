# Queues 🚽  

## Queues
- FIFO: first-in, first-out - this means the oldest element, the item added first, is the first item to be removed

## Real World Example
- Bathroom queue/line 🚽🚶🏻‍♀️🚶🏽‍♂️ - the first person in line gets to go to the bathroom first
- Line at the DMV 

## Use cases
- Similar to LL and are typically used for breadth-first-searches for trees
- Might see this used to implement a cache

## Time Complexity
- Removing from the front is O(n)

## Queue Methods
3 primary methods: enqueue, dequeue, peek, and several helper methods: isEmpty, get Length

- `enqueue()`: add item to the back of the queue
- `dequeue()`: remove the first item from the queue
- `peek()`: return the item at the FRONT of the queue (but don't remove it)
- `isEmpty()`: check whether the queue is empty
- `length()`: returns the length of the queue