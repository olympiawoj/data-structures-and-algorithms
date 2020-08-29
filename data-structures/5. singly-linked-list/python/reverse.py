from singly-linked-list.py import singly-linked-list

'''
While you are traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



#ITERATIVE
def reverse(self):
    '''
    Time: O(N)
    Space: O(1)
    '''
        
    prev = None
    currNode = self.head 
    nextTemp = None

    while currNode != None:
        nextTemp = currNode.next #save next
        currNode.next = prev  #reverse- point curr node to prev node

        prev = currNode
        currNode = nextTemp #prev node becomes node we're 
        
    while prev:
        print('value', prev.value)
        prev = prev.next
        
    #new head of the list
    return prev

# RECURSIVE

def reverseList(self, head: ListNode) -> ListNode:

    '''
    1. Swap prev and next pointers for all nodes
    2. Change prev of head and change head pointer in the e
    '''
    prev = None
    currNode = head

    # at v top call, have node I'm sitting at
    # reverse rest of list, not including me
    # Each node does that until we get to the last node
    # This will not have a value until we get the bottom of the call stack
    # THEN we're going to 
    if currNode == None or currNode.next == None:
        return currNode
        
    newHead = self.reverseList(currNode.next)
    currNode.next.next = head
    currNode.next = None
    return newHead