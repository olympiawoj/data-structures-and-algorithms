from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    What are keys in the dictionary? Key is value, value is # of times, 
    So what's diff from LL and dictionary, in a LL you can access individual O(1) of O(n)
    Idea of having dict is - cache - is to say, limited # of space to store each element and get rid of things not used recently
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        # Empty storage dict dict
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
      1) is this value is in the cache?
        True? --- return value of the node that the dict is pointing to
        False ? --- return - if not, move it to head 
  
    if key is dict is false, return -1
    if key is in dict, create a node with the value of that key ('a','b' , 'c')
    Move that to the END of the DLL (head) - self.dll.move_to_end
    Then return the value of node 
    """

    def get(self, key):
        # is key in the dict?

        if self.size is 0 or key not in self.storage:
            return None

        if key in self.storage:
            # If the key is in the dict, create a constant value associated with that key
            print(self.storage[key].value)
            node = self.storage[key]
            # print(node.value)
            # Move that value to the end of DLL
            self.dll.move_to_end(node)

            # Return value of Node
            print('node value 1', node.value[1])
            print('node value 0', node.value[0])
            return node.value[1]
        # else if key is not in dict
        else:
            # Else return none
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # If the key is already in cache, move it to the end (newest)
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
            return
        # If we are at our limit of 10 items, then remove the head(oldest)
        # Make the size smaller
        if self.size == self.limit:
            del self.storage[self.dll.head.value[0]]
            self.dll.remove_from_tail()
            self.size -= 1
        # If key is not in cache and we are not at our limit
        # Add to tail the key value pair
        # Add to storage
        # Increase size by one
        self.dll.add_to_tail((key, value))
        self.storage[key] = self.dll.tail
        self.size += 1


lru = LRUCache(3)
lru.set("item1", "1")
lru.set("item2", "2")
lru.set("item3", "3")
lru.set("item2", "4")
lru.get("item1")
lru.get("item2")