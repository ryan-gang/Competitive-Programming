from typing import List


class Solution:
    # Runtime: 224 ms, faster than 82.39% of Python3 online submissions.
    # Memory Usage: 18.4 MB, less than 46.37% of Python3 online submissions.
    # T : O(N), S : O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return s

    # Using bitwise inversion.
    # i from start, is swapped with -[i+1] (from end.)
    # ~i produces just that.
    def reverseStringBitWise(self, s):
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]


sol = Solution()
assert sol.reverseString(s=["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
assert sol.reverseString(s=["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
assert sol.reverseString(s=["a"]) == ["a"]
