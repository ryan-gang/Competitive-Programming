class Solution:
    """
    As s is comprised of only "a" and "b", for every s, we can just create 2
    subsequences one with all "a"s and another with all "b"s. And this would
    cover entire s. So worst case our answer would be 2. And best case is if s
    is empty, then answer would be 0. (But that is not a valid input). Another
    case can be that s itself is a palindrome. In which case our answer would be
    1. So first check if s is a palindrome, if it is so, return 1 else 2.
    """

    # Runtime: 20 ms, faster than 100.00%.
    # Memory Usage: 13.8 MB, less than 53.87%.
    # T : O(N), S : O(1)
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


if __name__ == "__main__":
    sol = Solution()
    assert (sol.removePalindromeSub("ababa")) == 1
