# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # Reflect across diagonal
        for row in range(N):
            for col in range(row, N):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # Reflect across X-axis
        for row in range(N):
            for col in range(N//2):
                matrix[row][col], matrix[row][N-1-col] = matrix[row][N-1-col], matrix[row][col]
