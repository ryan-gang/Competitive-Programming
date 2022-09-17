from typing import List


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]


# Runtime: 254 ms, faster than 94.78% of Python3 online submissions.
# Memory Usage: 14.4 MB, less than 71.68% of Python3 online submissions.
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for word in words:
            wordSet = set(word)
            mask = 0
            for char in wordSet:
                bitIndex = ord(char) - ord("a")
                mask = mask | (1 << bitIndex)
            d[(mask)] = max(d.get(mask, 0), len(word))
        maxVal = 0
        for i in d:
            for j in d:
                if not i & j:
                    maxVal = max(maxVal, d[i] * d[j])

        return maxVal
        # return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


# Master other solutions
