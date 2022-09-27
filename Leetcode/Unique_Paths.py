from functools import lru_cache


class Solution:
    # Runtime: 32 ms, faster than 93.66% of Python3 online submissions.
    # Memory Usage: 14.4 MB, less than 73.91% of Python3 online submissions.
    # T : O(N), S : O(N) (Call stack)
    @lru_cache(maxsize=None)
    def uniquePathsRecurse(self, m: int, n: int) -> int:
        if (m, n) == (1, 1):
            return 1
        elif m <= 0 or n <= 0:
            return 0

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    # Runtime: 68 ms, faster than 10.30% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 73.91% of Python3 online submissions.
    def uniquePathsIterative(self, m: int, n: int) -> int:
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            current = [0] * (n + 1)
            # Total Ways to come to current cell, is the
            # sum of paths to come to dp[i-1][j] and dp[i][j-1]
            # Left cell, and upper cell.
            for j in range(1, n + 1):
                if (i, j) == (1, 1):
                    current[j] = 1
                else:
                    current[j] = current[j - 1] + prev[j]
            prev = current

        return current[-1]

    # Runtime: 53 ms, faster than 40.27% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 98.30% of Python3 online submissions.
    # Unique ways to come to the entire 1st row and entire 1st col is "1". Always.
    # Now from 1, 1 : We can make turns. As we can only move down or right, ways to come to a cell,
    # is the ways to come to the cell on its left + ways to come to the cell on its top.
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


# Ref : https://leetcode.com/problems/unique-paths/
# discuss/267043/Python3-Solution-backtracking-with-memoization.
sol = Solution()

assert sol.uniquePaths(m=3, n=7) == 28
assert sol.uniquePaths(m=3, n=2) == 3
assert sol.uniquePaths(m=3, n=3) == 6
assert sol.uniquePaths(m=3, n=4) == 10
assert sol.uniquePaths(m=4, n=5) == 35
print(sol.uniquePathsIterative(m=100, n=100))
