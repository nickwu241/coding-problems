# https://leetcode.com/problems/merge-two-sorted-lists/description/
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
        """
        prev_head = c = ListNode(0)
        c.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = c.next
                c.next = l2
                tmp_l2 = l2.next
                l2.next = nxt
                l2 = tmp_l2
            c = c.next
        c.next = l1 or l2
        return prev_head.next
