# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
import string

class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = dict(zip(map(str, range(1, 27)), string.ascii_lowercase))
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                result.append(mapping[s[i-2:i]])
                i -= 3
            else:
                result.append(mapping[s[i]])
                i -= 1
                
        return ''.join(reversed(result))
