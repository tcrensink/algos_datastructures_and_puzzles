"""
https://leetcode.com/problems/merge-two-binary-trees/description/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #- return values are all the same/compatible type: a tree_node or None
        #- mergeTrees arguments have same form, everywhere they're called
        #- easily traced: although mergeTree calls spawn off, they don't affect the final return statement 
        #- because mergeTrees is a method (not a function), it requires the "self" keyword on calls 
    def mergeTrees(self,t1,t2):
        
        if t1 == t2 == None:
            return None
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        
        t = TreeNode(t1.val + t2.val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        return t
        