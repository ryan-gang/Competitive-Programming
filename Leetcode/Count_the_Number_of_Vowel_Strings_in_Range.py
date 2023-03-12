class Solution:
    # T : O(N), S : O(1)
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        count = 0
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.vowelStrings(words=["are", "amy", "u"], left=0, right=2) == 2
    assert sol.vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4) == 3
