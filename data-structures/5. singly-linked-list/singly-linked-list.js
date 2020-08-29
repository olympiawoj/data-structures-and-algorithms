
//Singly Linked List Node
class Node {
    constructor(value) {
        this.value = value;
        // at beginning, nothing comes after
        this.next = null;
    }
}



class LinkedList {
    constructor() {
        // initially head and tail pointers will be null until we add our first node
        this.head = null;
        this.tail = null;
        this.length = 0
    }

    isEmpty() {
        return this.length == 0
    }

    push(value) {
        //create new node
        const newNode = new Node(value)
        //if our list is empty, set both head and tail to newNode
        if (this.isEmpty()) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            //list has one node
            //set current pointer to new node
            this.tail.next = newNode;
            //update tail to point to new node
            this.tail = newNode
        }
        this.length++

    }

    pop() {
        //List is empty
        if (this.isEmpty()) {
            return null;
        } else if (this.length == 1) {
            //List has only one node
            const nodeToRemove = this.head;
            this.head = null;
            this.tail = null;
            this.length--;
            return nodeToRemove;
        } else {
            //There are mulitple nodes in the list
            //Start pointer at the head

            let currentNode = this.head;
            //We're removing the last node in the list
            const nodeToRemove = this.tail;
            // This will be our new tail
            let secondToLastNode;

            while (currentNode) {
                if (currentNode.next == this.tail) {
                    secondToLastNode = currentNode;;
                    break;
                }
                //Looping
                currentNode = currentNode.next;
            }
            secondToLastNode.next = null;
            this.tail = secondToLastNode;
            this.length--;
            return nodeToRemove;
        }
    }

    //3 cases
    // 1) index request is outside the bounds of list
    // 2) list is empty
    // 3) requesting the first or last element
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


const list = new LinkedList();
list.push("Emma");
list.push("Sarah");
list.push("Ivy");
list.print()
console.log(list.get(0).value) //Emma


