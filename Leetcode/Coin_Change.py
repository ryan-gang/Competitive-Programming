from typing import List


class Solution:
    """
    dp[i] is the fewest number of coins making up amount i, then for every coin in coins,
    dp[i] = min(dp[i], dp[i - coin] + 1).
    """

    # Runtime: 4019 ms, faster than 8.46% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 86.15% of Python3 online submissions.
    # T : O(amount * len(coins)), S : O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        default_value = float("inf")
        dp = [default_value for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                # if coin == i:
                #     dp[i] = i // coin
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        print(dp)
        return dp[amount] if dp[amount] != default_value else -1


sol = Solution()
assert sol.coinChange(coins=[1, 2, 5], amount=11) == 3
assert sol.coinChange(coins=[2], amount=3) == -1
assert sol.coinChange(coins=[1], amount=0) == 0
assert sol.coinChange(coins=[2, 5, 10, 1], amount=27) == 4
