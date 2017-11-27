# https://leetcode.com/problems/self-dividing-numbers/description/
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def selfDividingNumber(n):
            return all(d != '0' and n % int(d) == 0 for d in str(n))
        return list(filter(selfDividingNumber, range(left, right+1)))
