# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            ind,max_val = nums.index(max(nums)), max(nums)

            node        = TreeNode(max_val)
            nums_left   = nums[0:ind]
            nums_right  = nums[ind+1:]

            node.left   = self.constructMaximumBinaryTree(nums_left)
            node.right  = self.constructMaximumBinaryTree(nums_right)
            
            return node
        
       
        
        

