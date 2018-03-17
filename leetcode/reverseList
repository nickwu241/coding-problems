# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            # Save next.
            nxt = curr.next
            # Point backwards.
            curr.next = prev
            # Increment.
            prev = curr
            curr = nxt
        return prev
