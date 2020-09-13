
# Arrays 

## Linked List
- An array is a _contiguous_ chunk of memory that stores a _collection of data_ with _numeric keys or indexes_ from 0 to length-1. 

## Computer Memory
- A computer's memory is binary. By definition, it must have always values of either 0s or 1s. The way a computer handles memory is by allocating, marketing it, says this segment of memory belongs to this program and nothing else can touch it. 

## Steps of Creating an Array in Memory
1. Find a space that's not already claimed
2. Claim it
3. Put a value there

## Linked Lists vs. Arrays
- Arrays are also used to store a list of values, but does so in a _contiguous_ fashion. 
- Linked Lists store each element as an isolated _node_ represented by circles

## Space Complexity
- The most space efficient data structure because there's nothing else in it


# Big O - Worst Case
**Time**
- Access: O(1)
- Search: O(n)
- Insertion: O(n)
    - Add to front: O(n) because we have to scoot over everything starting at the index we're inserting into. In the worst case, we're inserting into the 0th index in the array (pre pending) so we have to scott over everything in the array - that's O(n) time.
    - Add to back: O(1) *unless* we haven't preallocated enough room for the array, then it's O(n)
- Deletion: O(n)
    - Delete from front: O(n) because in the worst case, we're deleting the 0th item item in the array so we have to scoot over everything else in the array - that's O(n) time
    - Delete from back: O(1)
**Space**
- O(N)


## Pros and Cons of Arrays
### Pros
- Cache-friendly
- Fast lookups: Retrieving the element at a given index takes O(1) time regardless of the length of the array
- Fast appends: Adding a new element at the end of the array takes O(1) time
### Cons
- Fixed Size: You need to specify how many elements you're going to store in your array head of time (unless you're using a fancy dynamic array)
- Costly inserts and deletes: You have to "scoot over" the other elements to fill in our close gaps, which takes worse case O(n) time
- O(n) length to delete from the front. 




Data structures built on arrays
Arrays are the building blocks for lots of other, more complex data structures.

Don't want to specify the size of your array ahead of time? One option: use a dynamic array.

Want to look up items by something other than an index? Use a hash map.