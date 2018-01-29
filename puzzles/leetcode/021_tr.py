# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        1 this can be done recursively (see other solutions)
        2 is this in place, or does l3 consume more memory?
        """
        
        # root = l3 = ListNode(0)
        root = ListNode(0)
        l3 = root
        
    while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
            
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
    
        return root.next
                
        