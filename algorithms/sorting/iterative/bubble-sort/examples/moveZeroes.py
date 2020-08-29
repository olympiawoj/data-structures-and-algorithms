'''

https://leetcode.com/problems/move-zeroes/submissions/

Runtime: 7392 ms, faster than 5.00% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.

'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] ==  0:
                    #swap with j+1
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        