
# Note: This Queue class is sub-optimal. Why?
# Bc it's not using a linked list, it's using an array
# denqueue add to front is inefficient - bc you have to reindex every el when you pop -> O(n)
# removing from front is expensive

class Queue():
    def __init__(self):
        self.queue = []
    
    def __repr__(self):
        return f'Queue:({repr(self.queue)})'
    
    def length(self):
        return len(self.queue)
    
    #adds item to queue FIFO
    def enqueue(self, value):
        self.queue.append(value)

    #removes element at index 0 - front of queue
    def dequeue(self):
        if self.length() > 0:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return self.length() == 0


movieQueue = Queue()
movieQueue.enqueue("Emma")
movieQueue.enqueue("Sarah")
movieQueue.enqueue("Maranda")
movieQueue.enqueue("Ivy")

print(movieQueue.length()) #4
print(movieQueue.peek()) #Emma
movieQueue.dequeue()
print(movieQueue.peek()) #Sarah
movieQueue.dequeue()
movieQueue.dequeue()
movieQueue.dequeue()
print(movieQueue.isEmpty()) #True
