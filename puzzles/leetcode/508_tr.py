# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # get_sum recursively finds sub-tree sums
        # once assembled, these values are compared and the values that occur most frequently are returned.
        # c doesn't *have* to be passed to get_sum, but is more clear as c is modified in the function.
        
        def get_sum(root, c):
            if root is None:
                return 0
            sum_val  = root.val + get_sum(root.left, c) + get_sum(root.right, c)
            c[sum_val] += 1
            return sum_val

        if root is None:
            return []
        
        c = Counter()
        get_sum(root, c)
        max_val = max(c.values())
        return [k for k in c.keys() if c[k] == max_val]

    