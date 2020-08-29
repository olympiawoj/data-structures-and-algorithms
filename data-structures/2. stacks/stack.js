class Stack {
    constructor() {
        this.stack = [];
    }
    length() {
        return this.stack.length;
    }
    push(item) {
        return this.stack.push(item);
    }
    pop() {
        return this.stack.pop();
    }
    peek() {
        let topItem = this.stack[this.length() - 1];
        return topItem
    }
    isEmpty() {
        return this.length() == 0;
    }
}


let books = new Stack();
console.log('books', books)
books.push("Book 1");
books.push("Book 2");
books.push("Book 3");
console.log('books', books)
console.log(books.peek());  //Book3
books.pop();  //Book3
console.log(books)
console.log(books.peek()); //Book2
console.log(books.length());
