
# Note: This Queue class is sub-optimal. Why?
# Bc it's not using a linked list, it's using an array
# denqueue add to front is inefficient - bc you have to reindex every el when you pop -> O(n)
# removing from front is expensive
# deqneueue removes from front 
# enqueue adds to back

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    def __repr__(self):
        for el in self.queue:
            return f"{el}"

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

    def __repr__(self):
        for el in self.stack:
            return f"{el}"