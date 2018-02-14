# https://leetcode.com/problems/validate-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(root, lower, upper):
            if not root:
                return True
            
            return lower < root.val < upper and validate(root.left, lower, root.val) and validate(root.right, root.val, upper)
        return validate(root, -math.inf, math.inf)
