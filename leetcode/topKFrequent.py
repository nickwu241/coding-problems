# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [item for item, _ in collections.Counter(nums).most_common(k)]
