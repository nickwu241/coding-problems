# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        
        def insert_helper(node, val):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert_helper(node.left, val)
            elif val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert_helper(node.right, val)
        insert_helper(root, val)
        return root
