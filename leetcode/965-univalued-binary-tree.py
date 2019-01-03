# https://leetcode.com/problems/univalued-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return True
            return node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)
