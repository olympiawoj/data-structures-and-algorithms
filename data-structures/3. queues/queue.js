class Queue {
    constructor() {
        this.queue = []
    }

    length() {
        return this.queue.length;
    }

    enqueue(item) {
        this.queue.push(item)
    }

    dequeue() {
        return this.queue.shift();
    }
    peek() {
        return this.queue[0]
    }

    isEmpty() {
        return this.length() == 0;
    }

}


const movieQueue = new Queue();
movieQueue.enqueue("Emma");
movieQueue.enqueue("Sarah");
movieQueue.enqueue("Maranda");
movieQueue.enqueue("Ivy");
console.log(movieQueue.length()); // 4
console.log(movieQueue.peek()); // Emma
movieQueue.dequeue();
console.log(movieQueue.peek()); // Sarah
movieQueue.dequeue();
movieQueue.dequeue();
movieQueue.dequeue();
console.log(movieQueue.isEmpty()); // true