# https://leetcode.com/problems/knight-dialer/description/
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        jump = [
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (3, 9, 0),
            (),
            (1, 7, 0),
            (2, 6),
            (1, 3),
            (4, 2)
        ]
        
        dp = [1]*10
        for _ in range(N-1):
            nxt = [0]*10
            for pos in range(10):
                for next_pos in jump[pos]:
                    nxt[next_pos] += dp[pos]
            dp = nxt
        return sum(dp) % (10**9 + 7)
