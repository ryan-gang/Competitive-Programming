# Runtime: 254 ms, faster than 94.78%.
# Memory Usage: 14.4 MB, less than 71.68%.
# T : O(N^2), S : O(N)
class Solution:
    def maxProduct(self, words: list[str]) -> int:
        d: dict[int, int] = {}
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


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
