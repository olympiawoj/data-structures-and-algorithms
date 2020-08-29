
# Arrays 

## Linked List
- An array is a _contiguous_ chunk of memory that stores a _collection of data_ with _numeric keys from 0 to length-1. 

## Computer Memory
- A computer's memory is binary. By definition, it must have always values of either 0s or 1s. The way a computer handles memory is by allocating, marketing it, says this segment of memory belongs to this program and nothing else can touch it. 

## Steps of Creating an Array in Memory
1. Find a space that's not already claimed
2. Claim int
3. Put a value there

## Linked Lists vs. Arrays
- Arrays are also used to store a list of values, but does so in a _contiguous_ fashion. 
- Linked Lists store each element as an isolated _node_ represented by circles

## Space Complexity
- The most space efficient data structure because there's nothing else in it


# Big O - Worst Case
**Time**
- Access: O(1 )
- Search: O(n)
- Insertion: O(n)
    - Add to front: O(n)
    - Add to back: O(1) *unless* we haven't preallocated enough room for the array, then it's O(1)
- Deletion: O(n)
    - Delete from front: O(n)
    - Delete from back: O(1)
**Space**
- O(N)


## Pros and Cons of Arrays
### Pros
- Cache-friendly
### Cons
- O(n) length to delete from the front. 




