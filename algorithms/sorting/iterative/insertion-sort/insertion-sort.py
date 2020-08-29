import random

# l = list(range(100))
# random.shuffle(l)
# print('shuffled list', l)

l = [5, 3, 1, 6]


def insertion_sort(list):
    # Separate first element from the rest of the array. # Think about it as a sorted list of of one element
    #2,      K, 5, 9, J, 4

    # For all other indices, beginning with [1]:
    # Iterate to each other item that's AFTER this
    for i in range(1, len(list)):

        # a) Copy the item at that index into a temp variable
        # Temp equals k in this case
        temp = list[i]

        # b) Iterate to the left until you find the correct index in the "sorted" part of the array.

        #2, K,       5, 9, J, 4
        j = i
        while j > 0 and temp < list[j - 1]:
            print(f"i:{i}, j: {j}, temp: {temp}")
            # Shift items over to the right AS you iterate
            # Take j and scoot it over check until first item is smaller than second item
            list[j] = list[j-1]
            j -= 1

            print('list after each loop', l)
        # c) When the correct index is found, copy temp into this position
        list[j] = temp
        print('list when done', list)

    return list


print(insertion_sort(l))