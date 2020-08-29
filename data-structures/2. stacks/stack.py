
"""
LIFO  - last in first out
Like a book stack --> add a book, thats last it, will be the first out

pop --> remove from top/end
push --> add/append to top of stack/end

"""
class Stack():

    def __init__(self):
        self.stack = []
    
    def __repr__(self):
        return f'Stack:({repr(self.stack)})'

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.length() > 0:
            return self.stack.pop()
        else:
            return None

    def length(self):
        return len(self.stack)

    def peek(self):
        return self.stack[self.length() -1 ]
    
    def isEmpty(self):
        return self.length() == 0

    

books = Stack()

books.push("Book 1")
books.push("Book 2")
books.push("Book 3")
print(books.peek()) #Book 3
print(books.isEmpty())
print(books)
books.pop() #Book3
print(books.peek()) #Book2
print(books.length()) #2