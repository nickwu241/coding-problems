# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = second_max = 0
        max_i = -1
        for i, num in enumerate(nums):
            if num > max_num:
                second_max = max_num
                max_num = num
                max_i = i
            elif num > second_max:
                second_max = num

        return max_i if max_num >= 2*second_max else -1
