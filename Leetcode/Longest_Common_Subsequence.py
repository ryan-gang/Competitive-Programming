class Solution:
    """
    dp[i][j] is the length of the LCS between words1[0:i+1] and words2[0:j+1].
    If words1[i] and words2[j] are equal we can increment the length of LCS
    from words1[0:i] and words2[0:j] by 1.
    Or if its at the border, set to 1.
    Else carry forward the longest length till now.
    """

    # Runtime: 1231 ms, faster than 20.65%.
    # Memory Usage: 22.8 MB, less than 42.03%.
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
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

    # Runtime: 1436 ms, faster than 29.44%.
    # Memory Usage: 22.8 MB, less than 42.66%.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                top = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                if text1[i] == text2[j] and i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                elif text1[i] == text2[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(top, left)
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonSubsequence(text1="abcde", text2="ace") == 3
    assert sol.longestCommonSubsequence(text1="abc", text2="abc") == 3
    assert sol.longestCommonSubsequence(text1="abc", text2="def") == 0
    assert sol.longestCommonSubsequence(text1="a", text2="ace") == 1
    assert sol.longestCommonSubsequence(text1="a", text2="a") == 1
    assert sol.longestCommonSubsequence(text1="a", text2="e") == 0
    assert sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert sol.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2
