# Insertion Sort

## Overview
- **Definition:** A *in-place* sorting algorithm that *builds* the final sorted array *one item at a time* by dividing our array intwo two splitting the array into a sorted array of 1 element and an unsoprted array, then taking each element and INSERTing it where it should go in the shorted half.

- It's called insertion sort bc we're taking an el one at a time and inserting in the correct spot.

## Time & Space Complexities

### Worst Case 
- Time: O(N^2)
- Space: O(1)

### Best Case
- O(N)
- Best to use when the data is nearly sorted (because it is adaptive) or when the problem size is small (because it has low overhead).

## Example - Playing Cards
- 2,           K, 5, 9, J, 4
- 2, K          5, 9, J 4
- 2, 5, K        9, J, 4
- 2, 5, 9, K       J, 4
- 2, 5, 9, J, K       4
- 2, 4, 5, 9, J, K  —→ SORTED LIST


## Pseudocode 
1. Start with:
- A sorted list on the left of 1 element (index 0)
- An unsorted list on the right of several elements
2. Loop over every item in the unsorted list, starting at index 1
3. Copy that item into a temp variable
4. Iterate to the LEFT until you find the correct index in the "sorted" part of the array
5. Shift items to the right AS you iterate

3. Repeat


**Insertion Sort Psuedocode**

- Start by picking second el in the array (sorted portion is first element in index 0)
- Now compare the second element with the one before it and swap if necessary
- Continue to the next element and if it is in the incorrect order, iterate through the osrted portion (i.e. the left side) to place the element in the correct place
- Repeat until the array is sorted