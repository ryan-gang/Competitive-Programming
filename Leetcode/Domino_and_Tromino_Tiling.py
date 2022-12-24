# https://archive.ph/KZUmz


class Solution:
    # Runtime: 42 ms, faster than 82.6%.
    # Memory Usage: 13.9 MB, less than 85.40%.
    # T : O(N), S : O(N)
    def numTilings(self, N: int) -> int:
        """
        Very interesting logic behind the code.
        The archive link at the top should help.
        DP question, but with a twist.
        """
        M = 10**9 + 7
        dp = [1 for i in range(N + 1)]
        if N >= 2:
            dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= M

        print(dp)
        return dp[N]


if __name__ == "__main__":
    sol = Solution()
    assert sol.numTilings(1) == 1
    assert sol.numTilings(3) == 5
    assert sol.numTilings(4) == 11
    assert sol.numTilings(30) == 312342182
