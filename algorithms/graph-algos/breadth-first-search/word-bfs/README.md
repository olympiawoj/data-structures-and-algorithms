# Word Ladder II (Leetcode Problem)

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

- Only one letter can be changed at a time
- Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
- Return an empty list if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.


Example 1:
```python
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```


Example 2:
```python
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```


Goal = find all shortest transformation sequence(s) from beginWord to endWord under certain conditions

#### What are the inputs, outputs, and variables?
- **Inputs:** Two words (`beginWord` and `endWord`) which represent the starting node and destinatino node AND a dictionary's word list
- **Output:**  A list of `results` with all shortest transformation sequence(s) from beginWord to endWord such that
    - Only 1 letter can be changed at a time
    - Each transformed word must exist in the world list. Note that beginWord is not a transformed word.
- **Functions**
    - get_neighbors
    - word_ladder
- **Variables**: we'll need a variable to track the `results` list that we will return 

### Three Steps for solving ANY graph problem
1. Translate the problem into graph terminology
    - What are the nodes? All words in our graph - they may not be connected, but they're still in the same graph
    - What are the edges? Relationships between words which differ by 1 letter
    - Is it directed or undirected? Undirected
    - Is it cyclical or acyclical? Cyclic because you can go from bat -> ban -> bin -> bit -> bat
    - Is it weighted or unweighted? Unweighted 
    - Dense or Sparse, ratio of edges to modes? Sparse - one word only goes to a handful of other words
2. Build your graph 
3. Traverse your graph - using DFS or BFS
- **SHORTEST** word is biggest clue for Breadth first search. DFS will give you a valid path, but it won't necessarily give you the shortest path.  


58.47 in Graphs II video 
### Build the Graph 
- We don't need to build an entire graph and put all of our words into the adjacencyList - we can,  but it might be overkill. Instead all we need to do is implmenet this get_neighbors function. 
- Neighbors are the same as an _edge_ - it's all words that are 1 letter away. 

1. Load words from the dictionary by _open_ing a file and _read_ing it. 
    - The open function is used to open files _in our_ system. It takes two arguments - the _name_ of the file and the _mode_ for which indicates how the file will be opened - `r` for reading (or by default `r`)
    - Set equal to a variable to `f` which indicates file
    - Read the file object with `f.read()` - also make sure we lowercase and split on newlines
    - Create a `set` of _unique_ _unordered_ words and set equal to above
    - Close the file with `f.close()`
2. Create a function `get_neighbors` which gets all the words that are one letter away from the given word i.e. gets the EDGES. 
    - INPUT: A word that you want to get the neighbors of
    - OUTPUT: A results list of words that are one letter away from the given word
3. Create an empty array `results` which starts with words that have the same length first
4. Use the `list()` constructor and pass in a `word` to create a list of letters in the word that equal to a variable `list_word`
`"abc" = ["a", "b", "c"]`
5. Use a `for` loop to loop through the length of the list_word - `for in in range(len(list_word))`
6. Then, use a nested `for` loop to kiio through an array of every letter in the alpabet - `for letter in['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:`
7. For every letter in each word and every letter in the alphabet, create a copy of the `list_word.copy()` and set it equal to a variable `temp_word` 
8. Set `temp_word` at index `i`, each letter in the world, to the letter -> temp[i] = letter 
9. Create a variable `joined_word` and set it equal to an empty string `"".join(temp_word)`. This word joins the temp_word list into a string.
10. Check `if joined word in word_set and if joined_word != word:` 
    - If true, append `joined_word` to the `results` list
11. At thh end of the first for loop, `return results`
    





### BFS Algorithm - this will give us our shortest path 
1. Create a queue 
2. Enqueue a path to the starting word (starting with a node)  
    - Enqueue means add to the add to the back/end of queue
3. Create a [set](../data-structures/basics/set) to store visited vertices
4. Use `while` to loop until the queue is empty. While the queue is not empty:
    - Dequeue/remove the first PATH from the queue
    - Grab the vertex from the end of the path `v=path[-1]`
    - Check if that vertex has NOT been visited by seeing if its in our `visited` set
        - If it hasn't been visited, add it to the visited set `visited.add(v)` to mark it as visited
    - Check if this vertex is our target/destination vertex. 
        - If it is, return the path
    - Get all neighbors and loop over every neighbor. For every neighbor:
        - Make a copy of the path `path_copy = path.copy()`
        - Append the neighbor to the path i.e. the next node you visited `path.append(neighbor)`
        - Enqueue the copy / add to the queue so the loop runs again 
5. You will eventually finish looping either because 1) the vertex matched the target and returned the path OR 2) the vertex is not in the graph


### We are missing the get_neighbors() function 
- All we need to do is implmenet the get_neighbors function
- add_vertex, remove_vertex, add_edge, remove_edge - we don't need to do any of that 
- All we need to implement is get_neighbors 
