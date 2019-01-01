# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        stack = []
        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()
                op = operators[token]
                # Cast to int because truediv returns a float.
                stack.append(int(op(first, second)))
            else:
                stack.append(int(token))
        return stack.pop()
