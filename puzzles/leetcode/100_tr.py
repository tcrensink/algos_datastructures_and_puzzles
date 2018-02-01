# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        """
        - if p, q exist, recursively compare that their node values are equivalent
        - else, verify they are both None
        - if any of the above isn't satisfied, return False
        """
        if p and q:
            
            truth_val = bool(p.val == q.val)
            return truth_val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
           
        return p is None and q is None