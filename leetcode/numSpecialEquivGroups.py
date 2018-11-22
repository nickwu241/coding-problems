# https://leetcode.com/problems/groups-of-special-equivalent-strings/
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        group = set()
        for s in A:
            even = ''.join(sorted(s[0::2]))
            odd = ''.join(sorted(s[1::2]))
            group.add((even, odd))
        return len(group)
