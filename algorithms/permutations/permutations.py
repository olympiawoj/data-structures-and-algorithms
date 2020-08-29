# Return list of all permutations
# space - n!

def permute(nums):
    # Base case
    if len(nums) == []:
        return [[]]
    elif len(nums) == 1:
        return [nums]

    else:
        l = []
        for i in range(len(nums)):
            # Get each el, pre-pend to permutations of all remaining eleemnts
            
            #what we're interested in
            x = nums[i]
            #alll elements up to, not including first el then all elements after
            xs = nums[:i] + nums[i+1:] 
            print('x', x, 'xs', xs)
            #recurse           
            for p in permute(xs):
                l.append([x]+p)
        return l





print(permute([1, 2, 3]))
print(permute(['a', 'b', 'c']))


