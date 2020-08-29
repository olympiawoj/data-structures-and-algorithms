# Bubble Sort

## Overview
- **Definition:** A sorting algorithm where the *largest values bubble* up to the top, one at a time
- **Application:** - Loop through the entire array. For every item in the array, loop again to compare the item to it's neighbor. If they are out of order relative to eachother, SWAP! Then loop back to the beginning and keep going until no more swaps

## Time & Space Complexities
### Worst Case 
- Time: O(N^2)
- Space: O(1)

### Best Case
- Time: O(N) - data that's already nearly sorted
- Very small arrays

## Algorithm
- The way that bubble sort works is as we loop through each item
- We compare it to the one in front of it, the next item, and check is this larger than what we're comparing it to? If it is, we swap.
- You basically swap if something is larger and then compare it to the next one. Is it larger? Swap again.
- Not efficient or commonly used
That was our first pass all the way through the array and what happend is the largest values BUBBLE to the top. Now we repeat the process starting again at the beginning
As we go through, the amount of items we need to sort DECREASES. Our loops can reflect that. 

## Example

3, 2, 1
- Is 3 larger than 2? Yes - swap!
2, 3, 1
- Is 3 larger than 1? Yes - swap!
2, 1, 3
- Start over 
- Is 2 larger than 3? Yes - swap!
1, 2, 3

## How do we swap?

In Javacript:
``` javascript
//ES5
function swap(arr, index1, index2){
	//setup a temp variable to store index1, change index1 to be what's in index2
	//use temp variable to update array of index2
	var temp = arr[index1];
	arr[index1] = arr[index2];
	arr[index2] = temp;
}

//ES2016
const swap = (arr, index1, index2) => {
	[arr[index1], arr[index2]] = [arr[index2], arr[index1]];
}
```





## Python Psuedocode
1.  Define a function called `bubble_sort(arr):` that takes in an array
2. Start looping with variable i from 0 to `len(arr)`
3. Start an inner loop with variable j, from 0 to `len(arr)-1`, -1 so we don't go out of bounds bc we're comparing i to j 
4. Check `if arr[j] >arr[j+1]` 

## JavaScript Psuedocode 
1. Define a function called bubble sort that takes an array
2. **Start looping with a variable i at the end of the array towards the beginning** - we'll discuss why, has to do with the fact that we're shrinking down the amount of space that we're sortin
3. **Start an inner loop with variable j** from the beginning until i -1  (referring to first loop, nested loop depending on first loop)
4. **If arr[j]  is greater than arr[j+1], swap these two values-** whatever j is, we're going to compare it to the item ahead of it
4. @ the end, return the sorted array!

