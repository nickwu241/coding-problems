# https://leetcode.com/problems/sentence-similarity/description/
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        pair_set = set(map(tuple, pairs))
        return all(w1 == w2
                   or (w1,w2) in pair_set
                   or (w2,w1) in pair_set
                   for w1, w2 in zip(words1, words2))
