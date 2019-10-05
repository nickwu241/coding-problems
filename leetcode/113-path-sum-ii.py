# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result_paths = []
        self.getPaths(root, sum, [], result_paths)
        return result_paths
    
    def getPaths(self, node: TreeNode, sum: int, path: List[int], result_paths: List[List[int]]):
        if not node:
            return
        
        sum -= node.val
        path.append(node.val)
        if not node.left and not node.right and sum == 0:
            result_paths.append(list(path))
        self.getPaths(node.left, sum, path, result_paths)
        self.getPaths(node.right, sum, path, result_paths)
        path.pop()
