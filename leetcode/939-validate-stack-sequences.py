# https://leetcode.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not popped:
            return True
        elif len(pushed) > len(popped):
            return False
        
        stack = []
        popped_i = 0
        for pushed_item in pushed:
            stack.append(pushed_item)
            while stack and stack[-1] == popped[popped_i]:
                popped_i += 1
                if popped_i >= len(popped):
                    return True
                stack.pop()
        return False
