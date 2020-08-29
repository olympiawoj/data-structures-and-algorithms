from util import Stack

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]



def island_counter(matrix):
    #1) Initialize visited matrix
    visited = []
    for i in range(len(matrix)):
        #appended 6 of those into matrix, gives visited matrix 
        #[False, False, False, False, False], 
        #[False, False, False, False, False], 
        #[False, False, False, False, False], 
        #[False, False, False, False, False], 
        #[False, False, False, False, False], 
        #[False, False, False, False, False]] - each row has 5 elements and appended 6 to visited array
        visited.append([False] * len(matrix[0]))
    #2) Initialize island count
    island_count = 0 
    for col in range(len(matrix[0])): #matrix[0] returns a row and we're iterating over each column in the first row
        for row in range(len(matrix)): 
            #Check if node is not visited
            if not visited[row][col]:
                #If we create a 1 that has not been visited
                if matrix[row][col] == 1: 
                    #Mark it visited
                    #Incremenet visited count
                    #Traverse all connected nodes, marking as visited
                        #Pass in starting node- row, col - matrix, and visited. 
                    visited = dft(row, col, matrix, visited)
                    #Increment island_count 
                    island_count +=1


    
    return island_count



def dft(start_row, start_col, matrix, visited):
    """
    Do a DF traversal
    Return an updated visited matrix with all connected components marked as visited
    """
    s = Stack()
    #starting vertex tuple
    s.push((start_row, start_col ))
    while s.size() > 0:
            v = s.pop()
            row=v[0]
            col=v[1]
            #check if its been visited
            if not visited[row][col]:
                print(v)
                #mark as visited
                visited[row][col] = True
                #push all neighbors into stack
                for neighbor in get_neighbors(row, col, matrix ):
                    s.push(neighbor)
    #return an updated matrix with all connecrted components marked
    return visited     



def get_neighbors(row, col, matrix):
    '''
    Return a list of neighboring 1 tupples in the from of [(row, col)]

    row 1 (0-1), column 3(0, 1, 2, 3) - how do we get the neighbors of this given node 
    Look N, S, E, W - if there's a 1, add to our list , look row +1 and row  -1 , doenst matter N or S
    [matrix[row -1][col], matrix[row +1][col], matrix[row][col -1], matrix[row][col + 1]]
    make sure we don't go out of bounds

    '''
    neighbors = []
    #check north
    if row > 0 and matrix[row-1][col]:
        neighbors.append((row-1, col))
    #check south
    if row < len(matrix) -1 and matrix[row+1][col]:
        neighbors.append((row+1, col))
    #check east
    if col < len(matrix[0])-1 and matrix[row][col +1] ==1:
        neighbors.append((row, col+1))
    #check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((row, col-1))
    return neighbors



    
print(island_counter(islands)) #4