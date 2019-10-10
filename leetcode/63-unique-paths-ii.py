# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            if obstacleGrid[row][0] == 1:
                break
            grid[row][0] = 1
        
        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            grid[0][col] = 1
        
        for row in range(1, len(grid)):
            for col in range(1, len(grid[row])):
                if obstacleGrid[row][col] == 1:
                    continue
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        return grid[-1][-1]
