# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = i_begin = 0
        h = {} # letter -> index

        for i, c in enumerate(s):
            # check for duplicate
            if c in h and i_begin <= h[c]:
                i_begin = h[c] + 1
            else:
                longest = max(longest, i - i_begin + 1)

            h[c] = i

        return longest
