# https://leetcode.com/problems/unique-number-of-occurrences/
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occurrences_set = set()
        for occurrences in counter.values():
            if occurrences in occurrences_set:
                return False
            occurrences_set.add(occurrences)
        return True
