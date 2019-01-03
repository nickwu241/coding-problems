# https://leetcode.com/problems/house-robber-ii/description/
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob(nums, low, high):
            robbed = last_robbed = 0
            for i in range(low, high):
                robbed, last_robbed = max(nums[i] + last_robbed, robbed), robbed
            return robbed

        return max(rob(nums, 1, len(nums)), rob(nums, 0, len(nums) - 1))
