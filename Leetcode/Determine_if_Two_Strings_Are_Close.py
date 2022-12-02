from collections import Counter


class Solution:
    # Runtime: 350 ms, faster than 59.60%.
    # Memory Usage: 15.3 MB, less than 43.60%.
    # T : O(N), S : O(1) # Max 26 keys from alphabet.
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        We don't care about the chars, we only care about the count of each char. (Operation1)
        We can only swap chars amongst each other, so the keys of both counters should be same,
        else we won't be able to make them close.
        """
        if len(word1) != len(word2):
            return False
        d1 = Counter(word1)
        d2 = Counter(word2)
        return sorted(d1.values()) == sorted(d2.values()) and d2.keys() == d1.keys()

    def closeStrings1L(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())


if __name__ == "__main__":
    sol = Solution()
    assert sol.closeStrings(word1="abc", word2="bca")
    assert not sol.closeStrings(word1="a", word2="aa")
    assert sol.closeStrings(word1="cabbba", word2="abbccc")
    assert not sol.closeStrings(word1="uau", word2="ssx")
