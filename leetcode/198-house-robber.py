# https://leetcode.com/problems/house-robber/description/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        robbed = max(nums[0], nums[1])
        last_robbed = nums[0]
        for i in xrange(2, len(nums)):
            robbed, last_robbed = max(nums[i] + last_robbed, robbed), robbed
        return robbed
