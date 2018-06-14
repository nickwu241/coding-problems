# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def setPossibleBreaks(start):
            for w in wordDict:
                end = start+len(w)
                if end >= len(dp) or dp[end]:
                    continue
                if s[start:end] == w:
                    dp[end] = True
            
        dp = [False] * (len(s) + 1)
        setPossibleBreaks(0)
        for i in xrange(1, len(dp)):
            if dp[i]:
                setPossibleBreaks(i)
        return dp[-1]
