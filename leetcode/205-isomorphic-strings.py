# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c1_to_c2_map = {}
        c2_used = set()
        for c1, c2 in zip(s, t):
            if (c1 in c1_to_c2_map or c2 in c2_used) and c1_to_c2_map.get(c1) != c2:
                return False
            c1_to_c2_map[c1] = c2
            c2_used.add(c2)
        return True
