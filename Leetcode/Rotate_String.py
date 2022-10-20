class Solution:
    """
    We concatenate the rotated string, and see if the original string is a
    substring of this concatenated string or not.
    original = AB
    rotated = BA
    concatenated = BABA
    original can be found inside concatenated."""

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            return Solution.is_substring(s + s, goal)
        return False

    @staticmethod
    def is_substring(s1: str, s2: str) -> bool:
        """Return True if s2 is a substring of s1."""
        print(s1, s2)
        i = j = streak = longest_streak = 0
        m, n = len(s1), len(s2)
        while i < m and j < n:
            s, t = s1[i], s2[j]
            if s == t:
                streak += 1
                longest_streak = max(longest_streak, streak)
                j += 1
            elif j > 0:
                streak = 0
                i = i - j
                j = 0
            i += 1

        return longest_streak == n


if __name__ == "__main__":
    sol = Solution()
    assert sol.is_substring("abcdef", "abc")
    assert sol.is_substring("abcdef", "bcd")
    assert sol.is_substring("abcdef", "cde")
    assert sol.is_substring("abcdef", "def")
    assert not sol.is_substring("abcdef", "abcdf")
    assert sol.is_substring("aaaaabcdefghijabcdefghij", "aab")

    assert sol.rotateString(s="abcde", goal="cdeab")
    assert not sol.rotateString(s="abcde", goal="abced")
    assert not sol.rotateString(s="aa", goal="a")
    assert sol.rotateString(
        s="vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg",
        goal="fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf",
    )
