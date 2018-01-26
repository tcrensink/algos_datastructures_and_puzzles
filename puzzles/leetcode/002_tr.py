# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        root = ListNode(None)
        l3 = root
        div = 0
        
        """
        - only get node values if they exist
        - don't forget the div (carry) value!
        - 'root' is a label for the first node for reference at the end
        """
        while l1 or l2 or div:
            
            val = div
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:    
                val += l2.val
                l2 = l2.next
            
            div, mod = divmod(val, 10)
            
            l3.next = ListNode(mod)
            l3 = l3.next
            
        return root.next