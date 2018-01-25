# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        
        def traversal(root, l):
            if root is None:
                return None
            traversal(root.left, l)
            l.append(root.val)
            traversal(root.right, l)
            return root
        
        traversal(root)
        return l