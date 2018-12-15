# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [None] * len(A)
        start = 0
        end = len(A) - 1
        for integer in A:
            if integer % 2: # Odd
                result[end] = integer
                end -= 1
            else: # Even
                result[start] = integer
                start += 1
        return result
