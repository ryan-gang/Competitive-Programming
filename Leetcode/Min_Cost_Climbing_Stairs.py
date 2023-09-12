class Solution:
    # Runtime: 72 ms, faster than 76.48%.
    # Memory Usage: 13.9 MB, less than 75.93%.
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n + 1)]
        dp[0] = dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min([dp[j] + cost[j] for j in range(i - 2, i)])

        return dp[-1]

    """
    Like Climbing_Stairs, here also we can define the state of the nth stair, using only the
    n-1th and n-2th stairs. So the cost of coming to the nth stair is simply, the min of (cost
    of coming to the n-1th stair + cost of that (n-1)th step, or the cost of coming to the
    n-2th stair + cost of that (n-2)th step. This can be defined using only 2 variables, the
    dp array is useless.
    """
    # Runtime: 53 ms, faster than 99.05%.
    # Memory Usage: 14 MB, less than 75.93%.
    def minCostClimbingStairsSpaceOptimised(self, cost: list[int]) -> int:
        n = len(cost)
        prev = prevprev = 0
        for i in range(2, n + 1):
            current = min((prev + cost[i - 1]), (prevprev + cost[i - 2]))
            prevprev, prev = prev, current

        return prev
