from typing import List

"""
Until yesterday, if we had our buy at b, and today we see a lower price, we should absolutely make
our buy at current 'b'. Because the optimal previous profit that was possible has been achieved.
If there is a higher price in the future, we can still only gain by making our buy at lower prices.
So greedy should always work in this case."""


class Solution:
    # Runtime: 2519 ms, faster than 15.47% of Python3 online submissions.
    # Memory Usage: 25 MB, less than 38.39% of Python3 online submissions.
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit, max_profit = prices[0], 0, 0
        for price in prices:
            if price < buy:
                buy = price
                profit = 0
            else:
                profit = price - buy
                max_profit = max(profit, max_profit)

        return max_profit


sol = Solution()
assert sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
