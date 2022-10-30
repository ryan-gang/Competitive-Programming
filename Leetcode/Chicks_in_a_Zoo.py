class Solution:
    def NoOfChicks(self, N):
        dp = [0] * 36  # 1-indexed array, where dp[i] is the ith day.
        dp[1] = 1
        for i in range(2, 36):
            prev = dp[i - 1]
            children = dp[i - 6] if (i - 6) >= 0 else 0
            children = round((children / 3) * 2)
            dp[i] = (prev - children) * 3

        return dp[N]
