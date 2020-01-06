# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]
        
        if tomatoSlices % 2 == 1:
            return []
        
        if not (cheeseSlices * 2 <= tomatoSlices <= cheeseSlices * 4):
            return []
        
        # Assume make all smalls, find how many extra tomatoe slices are left.
        extraTomatoeSlices = tomatoSlices % (cheeseSlices * 2)
        # Make jumbos instead of smalls to use up all tomatoe slices.
        total_jumbo = extraTomatoeSlices // 2
        total_small = cheeseSlices - total_jumbo
        return [total_jumbo, total_small]
