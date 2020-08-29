//https://medium.com/better-programming/singly-and-doubly-linked-lists-in-javascript-7515f47c9f60s

//Doubly Linked List Node
class Node {
    constructor(value) {
        this.value = value;
        // at beginning, nothing comes after
        this.next = null;
        this.prev = null;
    }
}



class DoublyLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    isEmpty() {
        return this.length == 0
    }

    push(value) {
        const newNode = new Node(value)

        if (this.isEmpty()) {
            this.head = newNode
            this.tail = newNode
        } else {
            // our current tail is going to become
            // our 2nd to last node
            // it's next should point to our new tail -new Node
            this.tail.next = newNode
            newNode.prev = this.tail
            this.tail = newNode
        }
        this.length++
    }

    pop() {
        if (this.isEmpty()) {
            return null
        } else if (this.length == 1) {
            const nodeToRemove = this.head
            this.head = null
            this.tail = null
            return nodeToRemove
        } else {
            //there are mulitple nodes in the list
            let currentNode = this.head
            const nodeToRemove = this.tail
            //this will be our new tail
            let secondToLastNode
            while (currentNode) {
                if (currentNode.next == this.tail) {
                    secondToLastNode = currentNode
                    break
                }
                currentNode = currentNode.next
            }

            //our new tail will not have a next
            secondToLastNode.next = null
            // our current tail is being set to our new tail
            this.tail = secondToLastNode
            this.length--
            console.log('nodeToRemove', nodeToRemove)
            return nodeToRemove.value
        }
    }

    get(index) {
        if (index < 0 || index > this.length || this.isEmpty()) {
            return null
        }
        /* We want the first node */
        if (index == 0) {
            return this.head
        }

        /* We want the last node */
        if (index === this.length - 1) {
            return this.tail
        }

        /* We want a node somewhere in the list so we iterate*/

        let currentNode = this.head
        let iterator = 0
        while (iterator < index) {
            iterator++
            currentNode = currentNode.next
        }

        return currentNode
    }

    print() {
        let currNode = this.head
        while (currNode !== null) {
            console.log(currNode.value)
            currNode = currNode.next
        }
    }

}



const list = new DoublyLinkedList();
list.push("Emma");
list.push("Sarah");
list.push("Ivy");
list.print()
console.log(list.get(0).value) //Emma
console.log(list.pop()) //Ivy
