# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        char_array = []
        char_array_i = 0
        for char in s:
            if char == '(':
                stack.append(char_array_i)
            elif char == ')':
                start = stack.pop()
                char_array[start:] = char_array[start:][::-1]
            else:
                char_array.append(char)
                char_array_i += 1
        return ''.join(char_array)
