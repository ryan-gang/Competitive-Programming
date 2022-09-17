from typing import List


# Runtime: 278 ms, faster than 49.77%.
# Memory Usage: 14.6 MB, less than 76.28%.
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordSet = set(words)

        for word in words:
            for i in range(1, len(word)):
                suffix = word[i:]
                if suffix in wordSet:
                    wordSet.remove(suffix)

        length = 0
        for word in wordSet:
            length += len(word)
            length += 1

        return length


sol = Solution()
print(sol.minimumLengthEncoding(words=["time", "atime", "btime"]))
