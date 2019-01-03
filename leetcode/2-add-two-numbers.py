# https://leetcode.com/problems/add-two-numbers/description/
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
        sumNode = c = ListNode(0)
        while l1 or l2:
            if l1:
                c.val += l1.val
                l1 = l1.next
            if l2:
                c.val += l2.val
                l2 = l2.next
            
            if c.val >= 10:
                c.val -= 10
                c.next = ListNode(1)
            elif l1 or l2:
                c.next = ListNode(0)

            c = c.next
        return sumNode
