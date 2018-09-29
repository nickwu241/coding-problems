# https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        cur = 0
        results = []
        while cur < len(nums):
            target = -nums[cur]
            front = cur + 1
            back = len(nums) - 1
            while front < back:
                sumtwo = nums[front] + nums[back]
                if sumtwo < target:
                    front += 1
                elif sumtwo > target:
                    back -= 1
                else:
                    res = [nums[cur], nums[front], nums[back]]
                    results.append(res)
                    
                    while front < back and nums[front] == res[1]:
                        front += 1
                    while front < back and nums[back] == res[2]:
                        back -= 1
            
            while cur < len(nums)-1 and nums[cur] == nums[cur+1]:
                cur += 1
            cur += 1
        return results
