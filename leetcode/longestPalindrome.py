# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start = 0
        max_len = 1
        for i in range(len(s)):
            if i - max_len >= 1 and self.isPalindrome(s[i-max_len-1:i+1]):
                start = i - max_len - 1
                max_len += 2
                continue
            
            if i - max_len >= 0 and self.isPalindrome(s[i-max_len:i+1]):
                start = i - max_len
                max_len += 1

        return s[start:start+max_len]
                
    def isPalindrome(self, s):
        return s == s[::-1]
