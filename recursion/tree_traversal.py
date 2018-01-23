import random
"""
Generate a binary tree and write a few recursive algorithms to traverse it, performing various functions:
"""

# Tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Randomly generated tree (not BST)
class Tree:
	def __init__(self):




class Solution:
    def reproduceTree(self, root):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root.val is None:
            return None
        
        if root.val < L or root.val > R:
        
            return self.trimBST(root.left, L, R)
            return self.trimBST(root.right,L, R)
        
        else:
            return self.trimBST(root.left, L, R)
            return self.trimBST(root.right,L, R)
        