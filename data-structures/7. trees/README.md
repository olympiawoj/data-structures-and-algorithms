# Trees 🌲

### Trees
- Trees are a data structure that consist of _nodes_ in a _parent/child relationship_ with one _root_ node. 

### Tree Examples 
- Folders in an operating system 📁 e.g. 
    Username/
        Desktop/
            Coding Folder/     Personal Folder/
                file file           file file 
- HTML DOM
- A decision tree
-  [B-tree](https://en.wikipedia.org/wiki/B-tree), which is a self-balancing ordered variant of the BST. B-trees play a critical role in database and file system indexing.
- AVL tree, which is a self-balancing BST and the prefix tree, which is specialized for handling text.

### Trees vs. [Lists](../doubly-linked-list/README.md) 
- Lists are LINEAR- one line through our data structure
- Tree are NONLINEAR- they can branch and have multiple different pathways
- A singly linked list is a special case of a tree

### Trees vs. [Graphs](../graphs/README.md) 
- Trees are a subset of a graph. but a restricted form of a graph
- Any tree is a type of graph but not all graphs will be trees (e.g. trees have a root node while graphs do not, graphs can be _cyclic_ and _acyclic_ while trees are always _acyclic_)

### Tree Definitions
- **Root:** The top node in a tree
- **Child:** A node directly connected to another node when moving _away_ from the root
- **Parent:** The node above a child
- **Leaf:** A node with no children
- **Edge:** The connection between one node and another

### Tree Rules
- **All trees must have a root node.** A root node can never have any edges or links connecting to it.
- **Tree must flow in ONE direction** from root/parent to child (can never go from child to parent/root)

## Binary Tree Rules Rules
- **Binary Trees** can only AT MOST 2 CHILDREN NODES. It can have 0, 1, or 2 children. That's it. 
- This means a binary tree can only have 2 subtrees within.
- Same rules apply to **ternary** trees (3 children)


## Binary Search Trees Rules
- **## Binary Search Trees** are a special type of binary tree. 
- They excel at searching so we store sorted data in a particular way in a binary search tree which makes it easier to retrieve. 
- They are used to _store data that are SORTED in a a paricular way_



### What's _NOT_ a tree?
- A tree as ONE entry point/root. If there are more, then it is NOT a tree. 
- Nodes MUST reference their children. If nodes reference siblings or any nodes below them, it is NOT a tree
- All nodes have to move AWAY from the parent code, all arrows must point down


### How is the root element of a Binary Search Tree decided?
- **The first element added to a BST is the root of the tree.**
- However, doing it this way means that it's a very simple matter to end up with a lopsided BST. If we simply insert a monotonically ascending or descending sequence of values, then the tree would essentially flatten down to a linked list, and we'd lose all the benefits that a BST is supposed to confer. 
- Self-balancing variants of the BST exist in order to alleviate this exact problem. 

### Helpful Links:
- Base CS Podcast- Don't be stumped... by trees: https://www.codenewbie.org/basecs/13
- Base CS Article- How Not To Be Stumped By Trees: https://medium.com/basecs/how-to-not-be-stumped-by-trees-5f36208f68a7
- Base CS Podcast- Trees IRL: https://www.codenewbie.org/basecs/14


### What is the difference between a Search and a Traversal?
- A search and a traversal are processed exactly the same.  The difference is:
- **In a search:** we stop when we find what we were looking for, or when all nodes have been visited without finding it 
- **In a traversal:** we always keep going until we've visited every node 

### What is the difference between Breadth First and Depth First?
- **Depth First:** Pick one path at each branch and keep going DOWN/forward until we hit a dead end, then  backtrack and take the first branch we find. 
- **Breadth First:** We go by layers, one row deeper each time.  This means that we jump around a bit.

