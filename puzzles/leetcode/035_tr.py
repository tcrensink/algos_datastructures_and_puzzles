class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        O(n) solution ( O(log n) possible):
        """
        for j, num in enumerate(nums):
            
            if num == target or num > target:
                return j
            
        return j + 1
        
        