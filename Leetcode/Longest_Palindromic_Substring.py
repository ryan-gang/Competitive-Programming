# Runtime: 871 ms, faster than 87.02% of Python3 online submissions for ...
# Memory Usage: 13.8 MB, less than 99.46% of Python3 online submissions for ...
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand_pallindrome(i, j):
            while 0 <= i <= j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j)

        res = (0, 0)
        for i in range(n):
            b1 = expand_pallindrome(i, i)
            b2 = expand_pallindrome(i, i + 1)
            res = max(
                res, b1, b2, key=lambda x: x[1] - x[0] + 1
            )  # find max based on the length of the pallindrome strings.

        return s[res[0] : res[1]]


sol = Solution()
print(sol.longestPalindrome("abaabd"))

# The core logic of the algo is we will iterate over a string,
# and check if the present character is a palindrome centre or not.
# We will keep on checking if the characters on both sides of this
# char are same or not and try to extend this palindrome.
# We will keep track of the largest palindrome encountered till now.
# Time : O(N^2)
# Space : O(1)
# Ref : https://leetcode.com/problems/longest-palindromic-substring/discuss/2156659/Python-Easy-O(1)-Space-approach

# Further reading : https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm

# Official sol : https://leetcode.com/problems/longest-palindromic-substring/solution/

# DP : https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Two-pointers
