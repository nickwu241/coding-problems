# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        s = []
        self.pushAllLeft(root, s)
        while s:
            c = s.pop()
            result.append(c.val)
            if c.right:
                self.pushAllLeft(c.right, s)
        return result

    def pushAllLeft(self, node, stack):
        while node:
            stack.append(node)
            node = node.left
