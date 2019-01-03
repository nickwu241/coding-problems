# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        before_head = curr = ListNode(0)
        priority_q = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(priority_q)
        while priority_q:
            _, i, node = heapq.heappop(priority_q)
            curr.next = node
            if node.next:
                heapq.heappush(priority_q, (node.next.val, i, node.next))
            curr = curr.next
        return before_head.next
