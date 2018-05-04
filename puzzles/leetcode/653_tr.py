"""
- method traverse:
    - returns False if node is a leaf
    - if compliment is found, returns True
    - if not, adds root.val to set `vals` and recurses to children
"""

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = set()
        return self.traverse(root, k, vals)

    def traverse(self, root, k, vals):

        if root is None:
            return False

        if k - root.val in vals:
            return True
        else:
            vals.add(root.val)
            return self.traverse(root.left, k, vals) or self.traverse(root.right, k, vals)
