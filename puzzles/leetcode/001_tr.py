class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :notes:
        O(n) in time.  for each element, check if the complement exists in the hash table.
        #if not, add an entry: key, value = number, index        
        """
        num_dict = {}
        for j,num in enumerate(nums):
            
            complement = target - num
            
            if complement in num_dict:
                return [j,num_dict[complement]]         
            num_dict[num] = j
            
        return None
        

