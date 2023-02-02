from string import ascii_lowercase
from typing import List


class Solution:
    # Runtime: 50 ms, faster than 29.94%.
    # Memory Usage: 13.8 MB, less than 77.66%.
    # T : O(NK + NKLog(NK)), S : O(N)
    # N words, K chars each.
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        original_order = ascii_lowercase

        sorted_words = sorted(
            words,
            key=lambda word: "".join(list(map(lambda w: original_order[order.index(w)], word))),
        )

        return sorted_words == words

    def isAlienSorted1L(self, words: List[str], order: str) -> bool:
        return words == sorted(
            words,
            key=lambda word: "".join(list(map(lambda w: ascii_lowercase[order.index(w)], word))),
        )

    def isAlienSorted1L2(self, words: List[str], order: str) -> bool:
        """
        No need to create the word in original order, just sort it based on custom order.
        """
        return words == sorted(words, key=lambda word: [order.index(c) for c in word])

    def isAlienSorted2(self, words: List[str], order: str):
        ord_d = {l: i for i, l in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for i, j in zip(w1, w2):
                if i != j:
                    if ord_d[i] > ord_d[j]:
                        return False
                    break
            if w1.startswith(w2) and w1 != w2:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
    assert not sol.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
    assert not sol.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
