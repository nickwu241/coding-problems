# https://leetcode.com/problems/find-bottom-left-tree-value/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return cur.val
