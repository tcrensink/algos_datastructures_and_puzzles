# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        - (base condition) return value 0 if node doesn't exist
        - if root has a left child and it's a leaf, return the left value and a recursive call to the right leaf:
        - otherwise: make a recursive call to both leaves
        - in all cases, function will either call itself again or return an integer        
        """ 
        if root is None:
            return 0
        
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
