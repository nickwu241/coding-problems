# https://leetcode.com/problems/binary-tree-pruning/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def all_zero(node):
            if not node:
                return True
            
            left_all_zero = all_zero(node.left)
            right_all_zero = all_zero(node.right)
            if left_all_zero:
                node.left = None
            if right_all_zero:
                node.right = None
            return node.val == 0 and left_all_zero and right_all_zero
        if all_zero(root):
            return None
        return root
