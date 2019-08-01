# https://leetcode.com/problems/distribute-candies-to-people/
import itertools

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        candies_to_give = 0
        for i in itertools.cycle(range(num_people)):
            candies_to_give += 1
            if candies <= candies_to_give:
                result[i] += candies
                return result
            
            candies -= candies_to_give
            result[i] += candies_to_give
