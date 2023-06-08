class Solution:
    # T : O(N*sqrt(N)), S : O(N)
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, (n := len(s)) // 2 + 1):
            substring = s[:i]
            if n % i == 0:  # Atmost sqrt(n) factors
                k = n // i
                if substring * k == s:
                    return True
        return False

    def repeatedSubstringPattern1(self, s: str) -> bool:
        """
        Pattern = AbAb
        Pattern x2 = AbAbAbAb
        Removing starting and ending characters = AxAbAbAx
        Pattern should be still present in this final string.
        """
        return s in (s * 2)[1:-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.repeatedSubstringPattern("abcdeabcde")
