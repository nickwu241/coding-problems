# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        blacklist = set()
        uncommon = set()
        for s in A.split() + B.split():
            if s in blacklist:
                continue
            if s in uncommon:
                uncommon.remove(s)
                blacklist.add(s)
                continue
            uncommon.add(s)
        return list(uncommon)
