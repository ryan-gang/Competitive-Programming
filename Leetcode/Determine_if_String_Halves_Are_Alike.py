class Solution:
    # Runtime: 71 ms, faster than 42.68%.
    # Memory Usage: 13.8 MB, less than 77.72%.
    # T : O(N), S : O(1)
    def halvesAreAlike(self, s: str) -> bool:
        s, n = s.lower(), len(s) // 2
        vowels = ["a", "e", "i", "o", "u"]
        vowel = 0
        for idx, val in enumerate(s):
            if val in vowels:
                if idx < n:
                    vowel += 1
                else:
                    vowel -= 1
        return vowel == 0


if __name__ == "__main__":
    sol = Solution()
    assert not sol.halvesAreAlike(s="textbook")
    assert not sol.halvesAreAlike(s="book")
