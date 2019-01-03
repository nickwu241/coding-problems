# https://leetcode.com/problems/fair-candy-swap/description/
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = 0
        setA = set()
        for candy_size in A:
            sumA += candy_size
            setA.add(candy_size)

        diff = sum(B) - sumA
        for candy_size in B:
            if candy_size - (diff / 2) in setA:
                return [candy_size - (diff / 2), candy_size]
