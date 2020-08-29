"""
1. Loop through your array
- Compare each element to its neighbor
- If elements in wrong position(relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
"""


def bubble_sort(arr):
    # Loop over ever item in the array
    for i in range(0, len(arr)):
        # For every item in array, compare it to it's neighbhor
        for j in range(0, len(arr) - 1):
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                print('swap', arr[j], arr[j+1])
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp
        print("ONE PASS COMPLETE")
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))