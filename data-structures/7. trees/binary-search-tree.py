'''
Binary Search - Programming equivalent of this, this algo crops ups a lot and its esp useful for when you want to look for some element or entry in some data that's already or almosrt sorted

O(log n)

- Recieves sorted array and target element we're looking for
- Typically start by finding midpoint of sorted array and comapre midpoint with target. If it matches, great, if not then we know if the target is less than the midpoint element, don't need to loook at the other half of the sorted array bc that'll contain elements that are larger than the element at midpoint we just looked at.
- We can reduce the amount of work we need to do
- As input size gets larger, the # of operations tapers off


'''

def binary_search(sorted_arr, target):
	low = 0, high = len(sorted_arr) -1
	midpoint = (high-low) //2
		if target == sorted_arr[midpoint]:
			return midpoint
		elif target < sorted_arr[midpoint]:
			return binary_search(sorted_arr[:midpoint])
		else:
			return sorted_arr[midpoint:]