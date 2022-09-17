# Runtime: 20 ms, faster than 100.00% of Python3 online submissions...
# Memory Usage: 13.8 MB, less than 53.87% of Python3 online submissions...
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if self.isPalindrome(s):
            return 1
        return 2

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# https://leetcode.com/problems/remove-palindromic-subsequences/discuss/2124240/One-Major-Observation-or-JAVA-Explanation

# https://leetcode.com/problems/remove-palindromic-subsequences/discuss/1099494/JS-Python-Java-C%2B%2B-or-Easy-Solution-w-Explanation

sol = Solution()
print(sol.removePalindromeSub("ababa"))
