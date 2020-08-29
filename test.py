def search(nums, target):
    low = 0
    high = len(nums) -1
    
    if not nums:
        return -1 

    while low <= high:

        mid = (high + low) // 2

        if nums[mid] == target: 
            return mid
            
        # if  our low is LESS than midpoint - left is sorted
        if nums[low] <= nums[mid]:
            # and our target is gerater than low, but lower than mid
            if nums[low] <= target  <= nums[mid]:
                #we know our new high is mid -1
                high = mid - 1
            else:
                low = mid + 1
                    
        #right is sorted
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high - mid - 1
        
    return -1




# nums = [4,5,6,7,0,1,2]
# target = 0

nums = [4,5,6,7,0,1,2]
target = 3

# 4 -> output

print(search(nums, target))