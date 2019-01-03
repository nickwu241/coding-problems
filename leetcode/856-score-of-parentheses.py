# https://leetcode.com/problems/score-of-parentheses/
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        running_sum = 0
        c = 1
        for i in range(1, len(S)):
            if S[i] == '(':
                c += 1
            elif S[i] == ')':
                c -= 1
                if S[i-1] == '(':
                    running_sum += 2 ** c
        return running_sum
