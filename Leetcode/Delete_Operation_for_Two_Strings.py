class Solution:
    # Runtime: 381 ms, faster than 54.24% of Python3 online submissions.
    # Memory Usage: 15.9 MB, less than 81.15% of Python3 online submissions.
    def minDistanceOld(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]

    # Runtime: 805 ms, faster than 7.56% of Python3 online submissions.
    # Memory Usage: 16.1 MB, less than 64.44% of Python3 online submissions.
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.longestCommonSubsequence(word1, word2)
        return len(word1) + len(word2) - (2 * lcs)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for __ in range(m)]
        for i, val_i in enumerate(text1):
            for j, val_j in enumerate(text2):
                if val_i == val_j and i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                elif val_i == val_j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]


sol = Solution()
assert sol.minDistance("sea", "eat") == 2
assert sol.minDistance("leetcode", "etco") == 4
assert sol.minDistance("s", "s") == 0
assert sol.minDistance("s", "a") == 2
