# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        s = [root]
        while s:
            c = s.pop()
            result.append(c.val)
            if c.right:
                s.append(c.right)
            if c.left:
                s.append(c.left)
        return result
