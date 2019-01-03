# https://leetcode.com/problems/climbing-stairs/description/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        f1, f2 = 1, 2
        for _ in xrange(3, n+1):
            r = f1 + f2
            f1 = f2
            f2 = r
        return r
