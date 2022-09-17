from typing import List


class Solution:
    # 88 / 136 TC passed. TLE.
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            n, flag = len(word), False
            lo, hi = 0, n - 1
            while lo <= hi:
                if word[lo] != word[hi]:
                    return False
                else:
                    flag = True
                lo, hi = lo + 1, hi - 1
            return flag

        n = len(words)
        out = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                concat = words[i] + words[j]
                if is_palindrome(concat):
                    out.append([i, j])

        return out


sol = Solution()
assert sol.palindromePairs(words=["abcd", "dcba", "lls", "s", "sssll"]) == [
    [0, 1],
    [1, 0],
    [2, 4],
    [3, 2],
]
