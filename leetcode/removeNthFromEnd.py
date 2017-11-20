# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        c = runner = head
        for _ in range(n):
            # always valid n so don't need to None check
            runner = runner.next

        if not runner:
            return head.next

        while runner.next:
            runner = runner.next
            c = c.next        
        c.next = c.next.next
        return head
