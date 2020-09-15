
# Linked Lists  ⚪️<-->⚪️ 

## Linked List
- At its core: a _linked list_ is just a collection of nodes
- A _linked list_ is a data structure that contains _nodes_ and each has a _value_ (string or num) and a _pointer_ to another node OR null
- Every _linked list_ contains a head, tail and length property

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
- A _Singly LL_ comes from the fact that each node is only connected one direction to the next node (except for the last node, points to NULL)
- A _Doubly Linked List_ list also has a connection pointing BACK to the previous node.
- A _Double Linked List_ usually tends to be better than a Singly Linked List because pointers are not expensive 

## Pros and Cons of Linked Lists
### Pros
- Linked Lists do NOT store elements contiguously and do NOT need to be allocated with a static amount of memory up front. This means we can keep adding eleemnts to linked lists as much as we want. 
- Easier to insert and delete from the middle of a LL versus an array 
### Cons
- Linked Lists are not cache-friendly since caches are typically organized for contiguous memory accesses



## Three Steps for creating a LL class
1. Nodes
    - How do weo insert 
    - What are the nodes?
    - What are the edges?
    - Is it directed or undirected?
    - Is it cyclical or acyclical?
    - Is it weighted or unweighted?
2. Linked List



### Doubly Linked Lists
 * The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
 * The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
   * `add_to_head` replaces the head of the list with a new value that is passed in.
   * `add_to_tail` replaces the tail of the list with a new value that is passed in.
   * `remove_from_head` removes the head node and returns the value stored in it.
   * `remove_from_tail` removes the tail node and returns the value stored in it.
   * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
   * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
   * `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
   * `get_max` returns the maximum value in the list. 
 * The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
 
![Image of Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)
