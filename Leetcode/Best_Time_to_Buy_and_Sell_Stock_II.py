from typing import List


class Solution:
    # Runtime: 146 ms, faster than 15.84% of Python3 online submissions.
    # Memory Usage: 15.2 MB, less than 69.25% of Python3 online submissions.
    # T : O(N), S : O(1)
    def maxProfit(self, prices: List[int]) -> int:
        """
        If there is a profit by buying yesterday and selling today, we take it.
        And repeat this daily. We always trade in 1d intervals. (No constraint on that.)
        But there is also a problem with this solution, often times we sell and buy on
        the same day, if there are bull runs on consecutive days, if this was disallowed,
        our solution would fail.
        """
        n = len(prices)
        profit = 0
        for i in range(1, n):
            curr_profit = prices[i] - prices[i - 1]
            if curr_profit > 0:
                profit += curr_profit

        return profit

    # Runtime: 60 ms, faster than 85.50%.
    # Memory Usage: 15.1 MB, less than 58.51%.
    # T : O(N), S : O(N)
    def maxProfit1(self, prices: List[int]) -> int:
        # Get positive profits for every 1D interval. Get sum of only positive profits.
        profits = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        positive_profits = list(filter(lambda val: val > 0, profits))
        return sum(positive_profits)

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solutions/
    # 803206/python-js-java-go-c-o-n-by-dp-greedy-visualization/
    # STATE MACHINE INTERPRETATION.
    def maxProfit2(self, prices: List[int]) -> int:
        # It is impossible to sell stock on first day,
        # set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float("inf"), 0

        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            # either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)
            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)

        # maximum profit must be in not-hold state
        return cur_not_hold


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
    assert sol.maxProfit(prices=[1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
