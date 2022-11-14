from functools import lru_cache


class Solution:
    # Runtime: 62 ms, faster than 12.68% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 12.83% of Python3 online submissions.
    # T : O(3 ^ N), S : O(N) (Without LRU Cache)
    # T : O(N), S : O(N) (With LRU Cache)
    def trib_helper(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def trib(n):
            if n <= 2:
                return [0, 1, 1][n]
            else:
                return trib(n - 1) + trib(n - 2) + trib(n - 3)

        return trib(n)

    # Runtime: 51 ms, faster than 62.34% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 59.57% of Python3 online submissions.
    # T : O(N), S : O(N)
    def trib3(self, n: int) -> int:
        if n <= 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        steps = [1, 2, 3]
        for i in range(1, n + 1):
            count = 0
            for step in steps:
                dist = i - step
                if dist >= 0:
                    count += dp[dist]

            dp[i] = count
        return dp[n - 1]

    # Runtime: 49 ms, faster than 47.36% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 12.83% of Python3 online submissions.
    # T : O(N), S : O(1)
    def trib2(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a

    # T : O(N), S : O(1)
    def tribonacci(self, n):
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]


if __name__ == "__main__":
    sol = Solution()
    assert sol.trib3(25) == 1389537
    assert sol.trib3(25) == 1389537
    assert sol.trib3(0) == 0
    assert sol.trib3(1) == 1
    assert sol.trib3(2) == 1
