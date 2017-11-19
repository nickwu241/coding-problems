# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        s = [(root, False)]
        while s:
            c, visited = s.pop()
            if visited:
                result.append(c.val)
                continue
            s.append((c, True))
            if c.right:
                s.append((c.right, False))
            if c.left:
                s.append((c.left, False))
        return result
