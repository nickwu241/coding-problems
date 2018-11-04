# https://leetcode.com/problems/shortest-bridge/description
from collections import deque

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """     
        def get_island(A, island, visited, node, n_rows, n_cols):
            if node in visited or A[node[0]][node[1]] == 0:
                return       
            visited.add(node)
            island.append(node)
            for new_node in get_neighbours(node, n_rows, n_cols):
                get_island(A, island, visited, new_node, n_rows, n_cols)
            return island
        
        def find_first_land(A, n_rows, n_cols):
            for row in range(n_rows):
                for col in range(n_cols):
                    if A[row][col] == 1:
                        return row, col
        
        def get_neighbours(node, n_rows, n_cols):
            row, col = node
            for nr, nc in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if 0 <= nr < n_rows and 0 <= nc < n_cols:
                    yield (nr, nc)
            
        n_rows, n_cols = len(A), len(A[0])
        visited = set()
        
        # Initialize BFS queue.
        q = deque()
        first_land = find_first_land(A, n_rows, n_cols)
        for node in get_island(A, [], visited, first_land, n_rows, n_cols):
            for row, col in get_neighbours(node, n_rows, n_cols):
                q.append((row, col, 1))

        # BFS.
        while q:
            row, col, steps = q.popleft()
            cur_node = (row, col)
            if cur_node in visited:
                continue

            if A[row][col] == 1:
                return steps-1

            visited.add(cur_node)
            for new_node in get_neighbours(cur_node, n_rows, n_cols):
                if new_node not in visited:
                    q.append((*new_node, steps+1))
