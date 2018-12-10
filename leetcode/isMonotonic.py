# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Check if it violates monotone decreasaing.
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                break
        else:
            # It is monotone decreasing.
            return True

        # Check if it violates monotone increasaing.
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        
        # It is monotone increasaing.
        return True
