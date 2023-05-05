class Solution:
    # Simple sliding window based approach.
    # T : O(N), S : O(1)
    def maxVowels(self, s: str, k: int) -> int:
        def handle_char(char: str, d: dict[str, int], addition: bool = True):
            # Add or remove char from the dict as required.
            condition = 1 if addition else -1
            if char in vowels:
                d["vowel"] += 1 * condition
            else:
                d["consonant"] += 1 * condition

        lo, hi = 0, k
        vowels = set(["a", "e", "i", "o", "u"])
        d = {"vowel": 0, "consonant": 0}

        for i in range(k):
            handle_char(s[i], d)

        max_vowels = d["vowel"]

        while hi < len(s):
            handle_char(s[hi], d)
            handle_char(s[lo], d, addition=False)
            lo, hi = lo + 1, hi + 1
            max_vowels = max(max_vowels, d["vowel"])

        return max_vowels


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxVowels(s="abciiidef", k=3) == 3
    assert sol.maxVowels(s="aeiou", k=2) == 2
    assert sol.maxVowels(s="leetcode", k=3) == 2
