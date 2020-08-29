class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node 
        self.length = 1 if node is not None else 0
    
    # def __repr__(self):
    #     return 'LinkedList: ({repr(self.length)})`

    def isEmpty(self):
        return self.length == 0

    def push(self, value):
        newNode = Node(value)

        # If our list is empty 
        # Set BOTH the head and tail to newNode
        
        if self.isEmpty():
            self.head = newNode 
            self.tail = newNode
        else:
            # list has at least one node
            self.tail.next = newNode
            self.tail = newNode 
        self.length +=1
            
    def pop(self):
        if self.isEmpty():
            return None
        elif self.length == 1:
            nodeToRemove = self.head
            self.head = None 
            self.tail = None
            self.length -= 1
            return nodeToRemove
        else:
            currentNode = self.head 
            #Remove our last node
            nodeToRemove = self.tail
            secondToLast = None 

            while currentNode:
                if currentNode.next == self.tail:
                    secondToLast = currentNode
                    break 
                #LOOP
                currentNode = currentNode.next
            secondToLast.next = None
            self.tail = secondToLast
            self.length -=1
            return nodeToRemove
    def get(self, index):
        #if the index is out of the bounds of the list
        # or if our list is empty
        if index < 0 or index > self.length or self.isEmpty():
            return None 
        #if we're requesting the last or first element
        if index == 0:
            return self.head 
        if index == self.length - 1:
            return self.tail
        #if we want a node somewhere in the list, iterate

        currentNode = self.head 
        iterator = 0
        while iterator < index:
            iterator +=1
            currentNode = currentNode.next
        return currentNode

    def print(self):
        currNode = self.head 
        while currNode != None:
            print(currNode.value)
            currNode = currNode.next
    


list = LinkedList()
list.push('Emma')
list.push('Sarah')
list.push("Ivy")
list.print()
print(list.get(0).value) #Emma