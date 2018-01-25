class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # trace tree; compliment of each value goes into a set
        # if element exists in set, change flag to true
        
        # to fix: flag must be contained in a list to be modified in traverse().  This is pretty inelegant.  Revise, try to revise using a flag in the first place...
        
        compliment = set()
        flag = [False]
        
        def traverse(root, k, flag):
                
            if root is None:
                return None
            
            if root.val in compliment:
                flag[0] = True
            else:
                compliment.add(k-root.val)
            
            print(root.val)
            
            traverse(root.left, k, flag)        
            traverse(root.right, k, flag)
            return root
        
        
        traverse(root, k, flag)
        return flag[0]        
        
        