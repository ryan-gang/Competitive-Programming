from collections import Counter


class Solution:
    # Runtime: 345 ms, faster than 5.00% of Python3 online submissions.
    # Memory Usage: 14.4 MB, less than 12.37% of Python3 online submissions.
    def canConstructNaieve(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        ransomNote.sort()
        magazine.sort()
        i, j = 0, 0
        while j < len(magazine) and i < len(ransomNote):
            if magazine[j] == ransomNote[i]:
                i += 1
            j += 1

        return i == len(ransomNote)

    # Runtime: 79 ms, faster than 65.70% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 53.79% of Python3 online submissions.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        return r < m

    def canConstructCleaner(self, ransomNote, magazine):
        return not Counter(ransomNote) - Counter(magazine)


sol = Solution()
assert not (sol.canConstruct(ransomNote="a", magazine="b"))
assert not (sol.canConstruct(ransomNote="aa", magazine="ab"))
assert sol.canConstruct(ransomNote="aa", magazine="aab")
