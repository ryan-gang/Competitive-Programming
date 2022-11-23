from typing import List


class Solution:
    """
    dp[i] is the number of ways we can count upto `amount` using a combination of coins.
    But this count can go wrong, we can count different permutations multiple times.
    Like dp[3] should include [1,1,1], and [1, 2]. But not [2, 1], because it's the same
    subsequence. So we need to enforce some order.
    We do that here, by looping over a specific coin at one time.
    So 1's at the beginning. Then all 2's. Then all 5's.
    This way we never calculate the same sequence twice.
    """

    # Runtime: 672 ms, faster than 50.15%.
    # Memory Usage: 14 MB, less than 90.63%.
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if (i - coin) >= 0:
                    dp[i] += dp[i - coin]

        print(dp)
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.change(amount=5, coins=[1, 2, 5]) == 4
    assert sol.change(amount=3, coins=[2]) == 0
    assert sol.change(amount=10, coins=[10]) == 1
