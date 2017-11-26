# https://leetcode.com/problems/asteroid-collision/description/
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for a in asteroids:
            if a < 0: # going left
                # check if the previous asteroid was going right
                while result and result[-1] > 0:
                    if -a > result[-1]: 
                        # destroy the asteroid going right
                        result.pop()
                    else: 
                        # we exploded
                        if -a == result[-1]:
                            result.pop()
                        break
                else: # previous asteroid going left
                    result.append(a)
            else: # going right since a is non-zero
                result.append(a)
        return result
