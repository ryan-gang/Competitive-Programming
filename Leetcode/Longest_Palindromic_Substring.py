class Solution:
    # Runtime: 871 ms, faster than 87.02%.
    # Memory Usage: 13.8 MB, less than 99.46%.
    # T : O(N^2), S : O(1)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand_palindrome(i: int, j: int) -> tuple[int, int]:
            while 0 <= i <= j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j)

        res = (0, 0)
        for i in range(n):
            # We consider each char in the string, to be a possible palindrome centre,
            # and try expanding it.
            b1 = expand_palindrome(i, i)
            b2 = expand_palindrome(i, i + 1)
            res = max(
                res, b1, b2, key=lambda x: x[1] - x[0] + 1
            )  # find max based on the length of the palindrome strings.

        return s[res[0] : res[1]]

    # T : O(N^2), S : O(N^2)
    def longestPalindromeDP2D(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # dp array
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = 1  # All strings of len = 1 are palindromes.

        # We need to do this to detect even length palindromes.
        # Else if we iterate for all diff's we will expand only from the odd centre.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                # i -> start, j -> end
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abaabd"))
