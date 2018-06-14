# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        self.setPossibleBreaks(s, wordDict, 0, dp)
        for i in xrange(1, len(dp)):
            if dp[i]:
                self.setPossibleBreaks(s, wordDict, i, dp)
        return dp[-1]
    
    def setPossibleBreaks(self, s, wordDict, start, dp):
        for w in wordDict:
            end = start+len(w)
            if end >= len(dp) or dp[end]:
                continue
            if s[start:end] == w:
                dp[end] = True
