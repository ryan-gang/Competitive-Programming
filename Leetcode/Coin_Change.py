import sys
from typing import List


class Solution:
    """
    dp[i] is the fewest number of coins making up amount i, then for every coin in coins,
    dp[i] = min(dp[i], dp[i - coin] + 1).
    Create amount (i - coin) with dp[i-coin] coins, then add 1 `coin` to that sequence.
    """

    # Runtime: 4019 ms, faster than 8.46%.
    # Memory Usage: 14.1 MB, less than 86.15%.
    # T : O(amount * len(coins)), S : O(amount)
    def coinChange1(self, coins: List[int], amount: int) -> int:
        default_value = sys.maxsize
        dp = [default_value for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != default_value else -1

    # Runtime: 3845 ms, faster than 38.39%.
    # Memory Usage: 14.2 MB, less than 86.39%.
    # T : O(amount*coins), S : O(amount)
    def coinChange(self, coins, amount) -> int:
        default = sys.maxsize
        dp = [default] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_value = dp[i]
            for coin in coins:
                if (i - coin) >= 0:
                    min_value = min(min_value, dp[i - coin])
            if min_value != default:
                dp[i] = min_value + 1
        return dp[-1] if dp[-1] != default else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange(coins=[1, 2, 5], amount=11) == 3
    assert sol.coinChange(coins=[2], amount=3) == -1
    assert sol.coinChange(coins=[1], amount=0) == 0
    assert sol.coinChange(coins=[2, 5, 10, 1], amount=27) == 4
