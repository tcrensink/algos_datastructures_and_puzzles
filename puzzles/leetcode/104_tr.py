# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        n = 0
        m = 0
        
        # base condition        
        if root is None:
            return 0
        
        # add 1 for each call, take max of left, right nodes 'coming back up'
        n = 1 + self.maxDepth(root.left)
        m = 1 + self.maxDepth(root.right)
        return max([n,m])
    
    
    