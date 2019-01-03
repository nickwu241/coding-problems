# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dc_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        combinations = [[]]

        # digits are [2-9] so don't need to check for invalid digits
        for d in digits:
            self.append_comb(combinations, dc_map[d])
        return [''.join(comb) for comb in combinations]

    def append_comb(self, combinations, chars):
        """Assumes len(combinations) > 0 and len(chars) > 0."""
        len_chars = len(chars)
        new_combinations = []
        for comb in combinations:
            for i in range(len_chars-1):
                new_comb = list(comb)
                new_comb.append(chars[i])
                new_combinations.append(new_comb)
            comb.append(chars[len_chars-1])
        combinations += new_combinations
