# Linked Lists  ⚪️-->⚪️ 

## Linked List
- At its core: a _linked list_ is just a collection of nodes
- A _linked list_ is a data structure that contains _nodes_ and each has a _value_ (string or num) and a _pointer_ to another node OR null
- Every _linked list_ contains a head, tail and length property


## LIFO
- Linked Lists use LIFO, similar to a stack, where nodes are added to and deleted from the same end

## Linked Lists vs. Arrays

### Linked Lists
- Linked Lists store each element as an isolated _node_ represented by circles. No indexing, just nodes pointing to the next element.
- Do not have indexes!
- Connects nodes via a next pointer
- Random access not allowed, we have to traverse all of `n` items 

### Arrays
- Each item is indexed with a number in order starting at 0 to length -1
- Insertion and deletion can be expensive 
- Can be quickly accessed at a specific index
- Stores values in a _contiguous_ fashion

## Doubly vs Singly

### Singly LL
- A _Singly LL_ comes from the fact that each node is only connected one direction to the next node (except for the last node, points to NULL)
- To remove a node from a Singly LL, we need to iterate through the list, keeping track of the previous node.

### Doubly LL 
- A _Doubly Linked List_ list also has a connection pointing BACK to the previous node.
- A _Double Linked List_ usually tends to be better than a Singly Linked List because pointers are not expensive 
- Doubly Linked Lists are great for removing nodes and reversing a LL because they provide access to previous and next nodes

## Pros and Cons of Linked Lists
### Pros
- Linked Lists do NOT store elements contiguously and do NOT need to be allocated with a static amount of memory up front. This means we can keep adding eleemnts to linked lists as much as we want. 
- Easier to insert and delete from the middle of a LL versus an array 
### Cons
- Linked Lists are not cache-friendly since caches are typically organized for contiguous memory accesses


# Big O - Worst Case
n = number of items in the list
**Time**
- Access: O(n)
- Search: O(n) - worst case, we start from the head node and iterate through each node until we reach the end of the list
- Insertion: O(1)
- Deletion: O(1)

**Space**
- O(N)

## Linked List Constructor
Our constructor keeps track of three things:
- `head`: the head pointer (keeps track of the first item in the LL)
- `tail`: the tail pointer (keeps track of the last item in the LL)
- `length`: the number of nodes in the list

## Linked List Methods
Linked lists use two primary methods (push, pop) and several helper methods (get index, delete, isEmpty);
- `push()`: Adds an element to the linked list
- `pop()`: Removes an element from the linked list
- `get(index)`: Returns an element from a given index (but doesn't remove it)
- `delete(index)`: Deletes an item from a given index
- `isEmpty()`: Returns a boolena indiciating whether the list is empty



REVERSE?
https://medium.com/the-core/how-to-recursively-reverse-a-linked-list-9990d59fc13f
        
        https://www.journaldev.com/30165/reverse-a-linked-list-c-python-implementation#reverse-a-linked-list-using-recursive-solution

https://www.geeksforgeeks.org/reverse-a-linked-list/

        1) Divide the list in two parts - first node and 
      rest of the linked list.
    2) Call reverse for the rest of the linked list.
    3) Link rest to first.
    4) Fix head pointer

https://leetcode.com/explore/interview/card/bloomberg/69/linked-list/431/discuss/58202/Python-solution-with-detailed-explanation


***
https://www.educative.io/edpresso/how-to-reverse-a-linked-list-in-python

