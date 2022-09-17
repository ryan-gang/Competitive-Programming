from functools import lru_cache


class Solution:
    # Runtime: 62 ms, faster than 12.68% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 12.83% of Python3 online submissions.
    def trib_helper(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def trib(n):
            if n <= 2:
                return [0, 1, 1][n]
            else:
                return trib(n - 1) + trib(n - 2) + trib(n - 3)

        return trib(n)

    # Runtime: 49 ms, faster than 47.36% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 12.83% of Python3 online submissions.
    def trib2(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a

    def tribonacci(self, n):
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]


# 0 -> 0
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 4
sol = Solution()
assert sol.trib(25) == 1389537
