# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Using backtracking, always add '(' and ')' when possible.
        ans = []
        self.generate(n, n, [], ans)
        return ans
        
    def generate(self, op: int, cl: int, current: List[str], ans: List[str]) -> None:
        if op == 0 and cl == 0:
            ans.append(''.join(current))
            return

        if op > 0:
            current.append('(')
            self.generate(op-1, cl, current, ans)
            current.pop()
        
        if cl > op:
            current.append(')')
            self.generate(op, cl-1, current, ans)
            current.pop()
