from util import Queue  


f = open('words.txt', 'r')
word_set = set(f.read().lower().split("\n"))
f.close()
def get_neighbors(word):
    '''
    Get all words that are one letter
    away from the given word i.e. get EDGES
    '''
    # Get same length words first
    results = []
    
    list_word = list(word)
    # Go through each letter in the word
    for i in range(len(list_word)):
        # swap with each letter in the alphabet
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            temp_word = list_word.copy()
            # Swap watch letter in the alphabet
            temp_word[i] = letter
            print(f"temp_word: {temp_word}")
            joined_word = "".join(temp_word)
            # If resulting word is in the word_set, add to results
            if joined_word in word_set and joined_word != word:
                print(f"joined_word: {joined_word}")
                results.append(joined_word)
    print(f'get_neighbors: {results}')
    return results

# 3: Traverse the graph (BFS)
def word_ladder(begin_word, end_word):
    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue( [begin_word] )
    # Create a visited set
    visited = set()
    # While queue is not empty:
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab the last word from the path
        w = path[-1]
        # Check if it's our target word
        if w == end_word:
            # If so, return path
            return path
        # Check if it's been visited
        # If not, mark as visited
        if w not in visited:
            visited.add(w)
            # Enqueue path to each neighboring word
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
print("HERE")
print(word_ladder("sail", "boat"))
print("END")
