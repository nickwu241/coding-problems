# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter()
        for first, second in dominoes:
            if first <= second:
                counter[(first, second)] += 1
            else:
                counter[(second, first)] += 1
        return sum(v * (v-1) // 2 for v in counter.values() if v >= 2)
