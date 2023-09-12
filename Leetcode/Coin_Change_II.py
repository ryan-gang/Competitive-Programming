from functools import cache


class Solution:
    """
    dp[i] is the number of ways we can count upto `amount` using a combination
    of coins. But this count can go wrong, we can count different permutations
    multiple times. Like dp[3] should include [1,1,1], and [1, 2]. But not
    [2, 1], because it's the same subsequence. So we need to enforce some order.
    We do that here, by looping over a specific coin at one time. So 1's at the
    beginning. Then all 2's. Then all 5's. This way we never calculate the same
    sequence twice.
    """

    # Runtime: 672 ms, faster than 50.15%.
    # Memory Usage: 14 MB, less than 90.63%.
    # T : O(M*N), S : O(N)
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        # for i in range(amount + 1):
        #     for coin in coins:
        #         # Gives wrong answer, because permutations are couned.
        #         # For val = 7 : (2,5) & (5,2) are counted.
        for coin in coins:
            for i in range(amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]

        return dp[-1]

    # T : O(M*N), S : O(N)
    def changeRecurse(self, amount: int, coins: list[int]) -> int:
        @cache
        def helper(amount: int, index: int) -> int:
            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0

            # Choose the coin
            choose = helper(amount - coins[index], index)

            # Don't choose the coin
            dontChoose = helper(amount, index + 1)

            return choose + dontChoose

        return helper(amount, 0)

    # T : O(M*N), S : O(M*N)
    def changeTabular(self, amount: int, coins: list[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # If amount = 0, there is 1 way to make change (by not choosing any coin)
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for coin in range(1, len(coins) + 1):
            for val in range(1, amount + 1):
                if val >= coins[coin - 1]:
                    dp[coin][val] = dp[coin - 1][val] + dp[coin][val - coins[coin - 1]]
                else:
                    dp[coin][val] = dp[coin - 1][val]

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.change(amount=5, coins=[1, 2, 5]) == 4
    assert sol.change(amount=3, coins=[2]) == 0
    assert sol.change(amount=10, coins=[10]) == 1
