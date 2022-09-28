from collections import Counter
from typing import List


class Solution:
    # Runtime: 472 ms, faster than 23.90% of Python3 online submissions.
    # Memory Usage: 15.3 MB, less than 34.52% of Python3 online submissions.
    # T : O(N), S : O(1)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        idx = window_size = len(p)
        # Can also use an array of length 26, instead of an hash-map.
        # But not a bit-array, possible values are not only 0 and 1.
        P = Counter(p)
        # Create counter of P, and create counter of sliding window of S.
        # If both counters are equal, add index to out.
        S = Counter(s[:window_size])
        if S == P:
            out.append(idx - window_size)

        for idx in range(window_size, len(s)):
            # This is the index of the new char added to the sliding window.
            # And we update the sliding window counter accordingly.
            # And check with the other counter.
            add_char = s[idx]
            del_char = s[idx - window_size]
            S[add_char] += 1
            S[del_char] -= 1
            if S == P:
                out.append(idx - window_size + 1)

        return out


sol = Solution()
assert sol.findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
assert sol.findAnagrams(s="abab", p="ab") == [0, 1, 2]
