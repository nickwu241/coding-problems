# https://leetcode.com/problems/add-one-row-to-tree/description/
from collections import deque

class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        
        q = deque([root])
        cur_depth = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur_depth == d - 1:
                    old_left = cur.left
                    old_right = cur.right
                    cur.left = TreeNode(v)
                    cur.right = TreeNode(v)
                    cur.left.left = old_left
                    cur.right.right = old_right
                else:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            cur_depth += 1
        return root
