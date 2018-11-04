# https://leetcode.com/problems/binary-subarrays-with-sum/description/
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        cur_sum = 0
        count = 0
        results = collections.Counter([0])
        for elem in A:
            cur_sum += elem
            count += results[cur_sum-S]
            results[cur_sum] += 1
        return count
