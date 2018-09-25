# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = deque([root])
        result = []
        should_reverse = False
        level_nodes = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if should_reverse:
                level_nodes.reverse()
            result.append(level_nodes)
            should_reverse = not should_reverse
            level_nodes = []

        return result
