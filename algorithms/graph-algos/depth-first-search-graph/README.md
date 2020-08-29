**The Algorithm**

1. Begin at the starting vertex (S)
2. Explore vertex

    a. If unexplored, adjacent vertex

    1. explore adjacent vertex

    b. Mark explored once all adjacent vertices have been explored (remove from stack)



    When is this a useful searching algo to use? We can use DFS to find both connected and strongly connected components within larger graphs


    **Key diff:** 


- DFS uses a **stack** instead of a queueto keep track of what nodes we explored/what nodes we've yet to explore

**To sum it all up**

- We can use DFS to traverse a graph **searching each branch to its deepest level** before exploring another branch
- Good if you are solving problem where you know th**e solution is very far from the root**
- With BFS you know you're going to process those leaf nodes/ nodes away from starting node V close to the end of our search
- With DFS you will process some of those earlier in your search so you could potentially come across your solution more quickly