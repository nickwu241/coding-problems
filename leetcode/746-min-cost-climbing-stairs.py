# https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l2, l1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            now = cost[i] + min(l2, l1)
            l2 = l1
            l1 = now
        return min(l2, l1)
    
    def minCostClimbingStairsDP(self, cost):
        n_costs = len(cost)
        totals = [None] * n_costs
        totals[0] = cost[0]
        totals[1] = cost[1]
        for i in range(2, n_costs):
            totals[i] = cost[i] + min(totals[i-2], totals[i-1])

        return min(totals[n_costs-2], totals[n_costs-1])
