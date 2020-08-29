
#Singly Linked List node
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

#Double Linked List  node
class DoublyLLNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next