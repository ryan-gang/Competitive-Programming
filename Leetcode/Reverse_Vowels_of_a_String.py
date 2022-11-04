class Solution:
    # Runtime: 145 ms, faster than 30.95% of Python3 online submissions.
    # Memory Usage: 15.2 MB, less than 33.93% of Python3 online submissions.
    # T : O(N), S : O(N)
    def reverseVowels(self, s: str) -> str:
        VOWELS = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        out = ["."] * len(s)

        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if s[lo] in VOWELS and s[hi] in VOWELS:
                out[lo], out[hi] = s[hi], s[lo]
                lo += 1
                hi -= 1
            elif s[lo] in VOWELS:
                out[hi] = s[hi]
                hi -= 1
            elif s[hi] in VOWELS:
                out[lo] = s[lo]
                lo += 1
            else:
                out[lo], out[hi] = s[lo], s[hi]
                lo += 1
                hi -= 1

        return "".join(out)

    """
    More cleaner than the previous implementation.
    """
    # Runtime: 98 ms, faster than 67.62% of Python3 online submissions.
    # Memory Usage: 15 MB, less than 85.41% of Python3 online submissions.
    def reverseVowels1(self, s: str) -> str:
        VOWELS = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        out = list(s)

        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < len(s) and out[lo] not in VOWELS:
                lo += 1
            while hi >= 0 and out[hi] not in VOWELS:
                hi -= 1
            if lo < hi:
                out[lo], out[hi] = out[hi], out[lo]
                lo += 1
                hi -= 1

        return "".join(out)


sol = Solution()
assert sol.reverseVowels1("leetcode") == "leotcede"
assert sol.reverseVowels1("hello") == "holle"
assert sol.reverseVowels1(" ") == " "
assert sol.reverseVowels1("aA") == "Aa"
assert sol.reverseVowels1(".,") == ".,"
