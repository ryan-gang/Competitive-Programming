class Solution:
    """
    dp[i] is the optimal product while adding upto i.
    dp[i] = for j in range(1, i // 2 + 2):
            max(j, self.dp[j]) * max((i - j), self.dp[i - j])
    """

    # Runtime: 112 ms, faster than 5.04% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 19.45% of Python3 online submissions.
    # T : O(N^2), S : O(N)
    def __init__(self) -> None:
        max_n = 58 + 2
        self.dp = [1 for _ in range(max_n)]
        for i in range(3, max_n):
            val = 0
            # print(i)
            for j in range(1, i // 2 + 2):
                # print(j, i - j)
                val = max(val, max(j, self.dp[j]) * max((i - j), self.dp[i - j]))
            self.dp[i] = val

    def integerBreak(self, n: int) -> int:
        return self.dp[n]


sol = Solution()
assert (sol.integerBreak(n=2)) == 1
assert (sol.integerBreak(n=10)) == 36
assert (sol.integerBreak(n=30)) == 59049
assert (sol.integerBreak(n=58)) == 1549681956
