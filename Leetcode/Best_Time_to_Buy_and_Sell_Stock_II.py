from typing import List


class Solution:
    """
    If there is a profit by buying yesterday and selling today, we take it.
    And repeat this daily.
    We always trade in 1d intervals.
    But there is also a problem with this solution, often times we sell and buy on the same day,
    if there are bull runs on consecutive days, if this was disallowed, our solution would fail."""

    # Runtime: 146 ms, faster than 15.84% of Python3 online submissions.
    # Memory Usage: 15.2 MB, less than 69.25% of Python3 online submissions.
    # T : O(N), S : O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1, n):
            curr_profit = prices[i] - prices[i - 1]
            if curr_profit > 0:
                profit += curr_profit

        return profit


sol = Solution()
assert sol.maxProfit([1]) == 0
assert sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
assert sol.maxProfit(prices=[1, 2, 3, 4, 5]) == 4
assert sol.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
