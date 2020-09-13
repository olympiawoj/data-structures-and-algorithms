# Stacks 📚 

- Stacks are 
- LIFO (FILO) - last in, first out. This means the newest element, added last to the stack, will be the first one to remove. 

## Real World Example
- Stack of books 🚽🚶🏻‍♀️🚶🏽‍♂️ - the last book on the top of the stack is first to get taken off
- Stack of dollar bills 

# Data Structure Implementation
- Linked List - double LL is always better than single bc pointers are not expensive 
- Array - if we use an array, the top of the stack will  be the right side of the array, the bottom of the stack will be the left side. 


# Big O - Worst Case
**Time**
- Access: O(n)
- Search: O(n)
- Insertion: O(1)
- Deletion: O(1)
**Space**
- O(N)

# Recursion
Which of these data structures are associated with problems that can be resolved recursively and why?  Recursion adds to the callstack, which is literally a stack


## Stack Methods
- `pop()`: Removes the top item from the stack
- `push(item)`: Adds item to the top of the stack
- `peek()`: Returnts the item at the top of the stack (does not remove it)
- `isEmpty()`: Returns true if the stack is empty
- `getLength()` Returns the number of items in the stack. 

What are real-world use-cases for a Stack data structure?

Stacks are used when you want to work with data Last in First Out (LIFO or FILO). They're used in processor architecture, undo logic, and depth first searches and traversals.