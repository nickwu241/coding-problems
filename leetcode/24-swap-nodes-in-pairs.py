# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        p, f, s = ListNode(0), head, head.next
        head = s
        while s:
            p.next, f.next, s.next = s, s.next, f
            if not f.next:
                break
            p, f, s = f, f.next, f.next.next
        return head
