# https://leetcode.com/problems/fizz-buzz/description/
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        fizz, buzz = 3, 5
        for num in range(1, n+1):
            fizz -= 1
            buzz -= 1
            numStr = ''
            if fizz == 0:
                numStr += 'Fizz'
                fizz = 3
            if buzz == 0:
                numStr += 'Buzz'
                buzz = 5
            result.append(numStr or str(num))
        return result
