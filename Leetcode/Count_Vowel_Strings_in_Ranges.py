from itertools import accumulate


class Solution:
    # T : O(N), S : O(N)
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        v_words = [0] * len(words)
        VOWELS = set(["a", "e", "i", "o", "u"])
        for idx, word in enumerate(words):
            if word[0] in VOWELS and word[-1] in VOWELS:
                v_words[idx] = 1

        prefix_v_words = list(accumulate(v_words))
        out = [0] * len(queries)

        for idx, query in enumerate(queries):
            val = 0
            l, r = query
            val += prefix_v_words[r]
            if l > 0:
                val -= prefix_v_words[l - 1]
            out[idx] = val

        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.vowelStrings(
        words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]
    ) == [2, 3, 0]
    assert sol.vowelStrings(words=["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]]) == [3, 2, 1]
