# Note: This Queue class is sub-optimal. Why?
# MUST BE IN SHELL FOR RPR TO WORK

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
