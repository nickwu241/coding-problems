# https://leetcode.com/problems/friend-circles/
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(i):
            if parents[i] == i:
                return i
            parent = find(parents[i])
            parents[i] = parent
            return parent
        
        # Make set for every node.
        n = len(M)
        parents = list(range(n))
        
        # Union node i and node j if they have an edge.
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    parents[find(i)] = find(j)
        
        # The number of friend circles is the number of sets.
        n_circles = 0
        for node, parent in enumerate(parents):
            if node == parent:
                n_circles += 1
        return n_circles
