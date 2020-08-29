# Sets 🥢

### Sets
- A collection of data that is _unordered_ and _unindexed_
- Set only stores a value once even if it is inserted more then once

### Three characteristics
- unordered
- set elements are unique, duplicate elements are not allowed
- a set itself may be modified, but the elements contained in the set must be of an immutable type 


### Syntax

### Initialze a Set
set = {"apple", "banana, "cherry"}
set() we can use the constructor to initialize an empty set

### Access elements in a set
for el in set:
    print(el)
print("apple" in set)

- You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
- But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
print("apple" in set) //true or false 

### Add elements to set
set.add("orange")
print(set)

### Get Length
print(len(set))

### Remove an element by item name
set.remove("apple")

## Remove the last item
- Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
set.pop()


**Set Properties**

- O(1) lookup, unordered, no repeats
- Set ONLY has keys. A set is a hash that only stores keys and no vaues, so it has all the properties of a dictionary except there's no values.
- Only UNIQUE values


https://www.w3schools.com/python/python_sets.asp



- You want O(1) - we're using a SET so we have NO duplicates. Every time we check a node, we check if its visited or not.
- As visited list grows, if we're using an array its going to be O(n) instead of O(1) lookup
- Array makes it turn into O(n^2) - visiting turns into O(n) and now our traversl is O(n^2) instead of O(n) bc set is O(1)
- Memory is cheap. Time is most expensive thing we have.



**Sets**

- Use curly brackets to create our sets
- Create a set of cities, I can add new cities to a set - single elements with add or use update to add multiple elements at a time
- CANNOT change items at a particular index like we could with lists bc with sets, there's not really a set order to how the items are being stored so don't have ability to reference items by an index, not assigned an index that will remain the same
- CAN remove items in a couple diff ways - by their value, we can pop to remove last item that was added to the set
- CAN grab the length len(set_name) and we can traverse the set using a for loop