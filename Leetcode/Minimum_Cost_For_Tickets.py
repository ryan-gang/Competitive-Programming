from collections import deque


class Solution:
    # T : O(N), S : O(1) ; Constant space for DP. 365 days max.
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        Bottom-up DP. Where each "travel" day we find out the optimal cost,
        using 1d, 7d and 30d pass.
        """
        dp = [0] * (days[-1] + 1)
        d1, d7, d30 = costs
        for i in range(1, len(dp)):
            if i in set(days):
                dp[i] = min(
                    dp[max(i - 1, 0)] + d1,
                    dp[max(i - 7, 0)] + d7,
                    dp[max(i - 30, 0)] + d30,
                )
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

    # T : O(N), S : O(1) ; Constant space for queue. 7, 30 days max.
    def mincostTickets1(self, days: list[int], costs: list[int]) -> int:
        """Store only the optimal costs for the last 7 and 30 day window,
        progressively push and pop from this deque."""
        cost = 0
        last7: deque[tuple[int, int]] = deque()  # (day, cost)
        last30: deque[tuple[int, int]] = deque()  # (day, cost)
        for day in days:
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()
            last7.append((day, cost + costs[1]))
            last30.append((day, cost + costs[2]))
            cost = min(cost + costs[0], last7[0][1], last30[0][1])
        return cost


if __name__ == "__main__":
    sol = Solution()
    assert (sol.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15])) == 11
    assert sol.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]) == 17
    assert sol.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[7, 2, 15]) == 6
    assert (
        sol.mincostTickets(
            days=[1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17, 19, 21, 24, 26, 27, 28, 29],
            costs=[3, 14, 50],
        )
        == 50
    )
