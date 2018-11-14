# https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        row0_zeroed = any((matrix[0][col] == 0 for col in range(n_cols)))
        col0_zeroed = any((matrix[row][0] == 0 for row in range(n_rows)))
        # Use the first row or first col to signify to zero out the row/col if needed.
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, n_rows):
            if matrix[row][0] == 0:
                for col in range(1, n_cols):
                    matrix[row][col] = 0
        
        for col in range(1, n_cols):
            if matrix[0][col] == 0:
                for row in range(1, n_rows):
                    matrix[row][col] = 0
        
        if row0_zeroed:
            for col in range(n_cols):
                matrix[0][col] = 0

        if col0_zeroed:
            for row in range(n_rows):
                matrix[row][0] = 0
