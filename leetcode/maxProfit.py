# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price_so_far = float('inf')
        for price in prices:
            if price <= min_price_so_far:
                min_price_so_far = price
            else:
                max_profit = max(max_profit, price - min_price_so_far)
        return max_profit
