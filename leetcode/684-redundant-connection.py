# https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n))
        ranks = [0] * n
        
        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False
            
            rank_u = ranks[root_u]
            rank_v = ranks[root_v]
            if rank_u == rank_v:
                ranks[root_u] += 1

            if rank_v > rank_u:
                root_u, root_v = root_v, root_u
            
            parents[root_v] = root_u
            return True

        # "find" and "union" are index based.
        # We need to -1 from the node id to get their index.
        for u, v in edges:
            if not union(u-1, v-1):
                return [u, v]
