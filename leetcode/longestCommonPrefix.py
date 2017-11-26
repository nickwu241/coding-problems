# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]

        min_slen = len(strs[0])
        for s in strs[1:]:
            min_slen = min(min_slen, len(s))

        i = 0
        while i < min_slen:
            c = strs[0][i]
            for s in strs[1:]:
                if c != s[i]:
                    return s[:i]
            i += 1

        return s[:i]
