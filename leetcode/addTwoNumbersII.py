# https://leetcode.com/problems/add-two-numbers-ii/
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
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        curr = ListNode(0)
        while s1 or s2:
            total = curr.val # 0 or 1 depending on carry.
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            curr.val = total % 10
            new_node = ListNode(1 if total >= 10 else 0)
            new_node.next = curr
            curr = new_node
        
        if curr.val == 0:
            return curr.next
        return curr
