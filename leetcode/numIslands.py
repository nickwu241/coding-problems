# https://leetcode.com/problems/number-of-islands/description/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def get_neighbors(row, col):
            neighbors = []
            if row-1 >= 0:
                neighbors.append((row-1, col),)
            if col-1 >= 0:
                neighbors.append((row, col-1),)
            if row+1 < n_rows:
                neighbors.append((row+1, col),)
            if col+1 < n_cols:
                neighbors.append((row, col+1),)
            return neighbors

        def fill_land(row, col):
            if grid[row][col] == WATER:
                return
            grid[row][col] = WATER
            for neighbor in get_neighbors(row, col):
                fill_land(*neighbor)

        if not grid or not grid[0]:
            return 0

        WATER, LAND = '0', '1'
        n_rows, n_cols = len(grid), len(grid[0])
        n_islands = 0
        for r in xrange(n_rows):
            for c in xrange(n_cols):
                if grid[r][c] == LAND:
                    n_islands += 1
                    fill_land(r, c)
        return n_islands
