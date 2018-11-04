# https://leetcode.com/problems/license-key-formatting/description/
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = []
        char_counter = 0
        i = len(S)-1
        while i >= 0:
            if S[i] == '-':
                i -= 1
                continue
            result.append(S[i].upper())
            char_counter = (char_counter+1) % K
            if char_counter == 0:
                result.append('-')
            i -= 1
        if result and result[-1] == '-':
            result.pop()
        return ''.join(reversed(result))
