class Solution:
    """
    dp[i][j] is the length of the LCS between words1[0:i] and words2[0:j].
    If words1[i] and words2[j] are equal we can increment that length.
    Or else carry forward the longest length till now.
    """

    # Runtime: 1231 ms, faster than 20.65% of Python3 online submissions.
    # Memory Usage: 22.8 MB, less than 42.03% of Python3 online submissions.
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
        # for i in dp:
        #     print(i)

        return dp[-1][-1]


sol = Solution()
assert sol.longestCommonSubsequence(text1="abcde", text2="ace") == 3
assert sol.longestCommonSubsequence(text1="abc", text2="abc") == 3
assert sol.longestCommonSubsequence(text1="abc", text2="def") == 0
assert sol.longestCommonSubsequence(text1="a", text2="ace") == 1
assert sol.longestCommonSubsequence(text1="a", text2="a") == 1
assert sol.longestCommonSubsequence(text1="a", text2="e") == 0
