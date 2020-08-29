"""Each ListNode holds a reference to its previous node
as well as its next node in the List.



https://www.pythoncentral.io/reverse-singly-linked-list/
https://www.youtube.com/watch?v=MRe3UsRadKw

"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def isEmpty(self):
        return self.length == 0

    def push(self, value):
        newNode = ListNode(value)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            #current tail will become 2nd to last node
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length+=1
    

    def swap(self, node):
        prev = node.prev
        node.prev = node.next
        node.next = prev 

    def reverse(self):
        '''
        1. Swap prev and next pointers for all nodes
        2. Change prev of head and change head pointer in the e
        '''
        prev = None
        currNode = self.head
        while currNode:
            self.swap(currNode)
            #update prev node before moving to next
            prev = currNode
            #advance using prev pointer, since next & prev were swapped
            currNode = currNode.prev
  
        if prev:
            self.head = prev

        return self.head
    
  
    def print_it(self):
        currNode = self.head
        while currNode:
            print(currNode.value) 
            currNode = currNode.next


    ## we can also do the reverse with recursionl.,..
list = DoublyLinkedList()
list.push("Emma")
list.push("Sarah")
list.push("Ivy")
list.print_it()
# print(list.get(0).value) //Emma
# print(list.pop()) //Ivy
list.reverse()
list.print_it()
