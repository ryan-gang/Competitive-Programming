from functools import lru_cache


class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        """
        Bottom-up DP.
        for every pile :
            for every value of k (coin) :
                curr_sum = 0
                for every value of coin (curr_coin):
                    sum up the top curr_coin coins from this pile.
                    Now dp[pile][coins] = max(dp[pile][coins],
                        curr_sum + dp[pile-1][coins-curr_coins])

        So, basically we are checking for each value of coin, taking coin values from this pile,
        and k - coins from the previous N piles.
        And we are storing the most optimal value in the dp array
        """
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for coins in range(0, k + 1):
                current_sum = 0
                for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                    if current_coins > 0:
                        current_sum += piles[i - 1][current_coins - 1]
                    dp[i][coins] = max(dp[i][coins], dp[i - 1][coins - current_coins] + current_sum)
        return dp[n][k]

    # T : O(k * S), S : O(n * k) ; where S is the total number of coins,
    # and n is the length of piles, used for dp.
    def maxValueOfCoins1(self, piles: list[list[int]], k: int) -> int:
        # Top down DP.
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def f(pile: int, coins: int) -> int:
            if pile == 0:  # If no piles, return 0.
                return 0
            if dp[pile][coins] != -1:  # If dp[pile][coins] is already calculated, return it.
                return dp[pile][coins]
            # If dp[pile][coins] is not calculated,
            # For the curr_coins values in range(0, coins):
            # Calculate the value we get from taking curr_coins coins from this pile,
            # and the rest optimally from the previous piles.
            curr_sum = 0
            for curr_coins in range(0, min(len(piles[pile - 1]), coins) + 1):
                if curr_coins > 0:
                    curr_sum += piles[pile - 1][curr_coins - 1]
                dp[pile][coins] = max(curr_sum + f(pile - 1, coins - curr_coins), dp[pile][coins])
            return dp[pile][coins]

        return f(n, k)

    def maxValueOfCoins2(self, piles: list[list[int]], k: int) -> int:
        # LRU Cache.
        n = len(piles)

        @lru_cache(maxsize=None)
        def f(pile: int, coins: int) -> int:
            if pile == 0:  # If no piles, return 0.
                return 0

            # For the curr_coins values in range(0, coins):
            # Calculate the value we get from taking curr_coins coins from this pile,
            # and the rest optimally from the previous piles.
            curr_sum = 0
            max_sum = -1
            for curr_coins in range(0, min(len(piles[pile - 1]), coins) + 1):
                if curr_coins > 0:
                    curr_sum += piles[pile - 1][curr_coins - 1]
                max_sum = max(curr_sum + f(pile - 1, coins - curr_coins), max_sum)
            return max_sum

        return f(n, k)
