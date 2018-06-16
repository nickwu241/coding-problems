# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        lowest_index = math.inf
        hm = {restaurant: i for i, restaurant in enumerate(list1)}
        for i, restaurant in enumerate(list2):
            if restaurant not in hm:
                continue
            
            if hm[restaurant] + i < lowest_index:
                lowest_index = hm[restaurant] + i
                result = [restaurant]
            elif hm[restaurant] + i == lowest_index:
                result.append(restaurant)

        return result
