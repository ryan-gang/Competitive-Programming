from collections import Counter
from typing import List


class Solution:
    # Runtime: 314 ms, faster than 43.80% of Python3 online submissions.
    # Memory Usage: 15.3 MB, less than 27% of Python3 online submissions.
    # T : O(N), S : O(1) (26 chars at most)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out: List[int] = []
        idx = window_size = len(p)
        # Can also use an array of length 26, instead of an hash-map.
        # But not a bit-array, possible values are not only 0 and 1.
        P = Counter(p)
        # Create counter of P, and create counter of sliding window of S.
        # If both counters are equal, add index to out.
        S = Counter(s[:window_size])
        if S == P:
            out.append(0)

        for idx in range(window_size, len(s)):
            # This is the index of the new char added to the sliding window.
            # And we update the sliding window counter accordingly.
            # And check with the other counter.
            add_char, del_char = s[idx], s[idx - window_size]
            S[add_char] += 1
            S[del_char] -= 1
            if S == P:
                out.append(idx - window_size + 1)

        return out

    # Runtime: 99 ms, faster than 95.29%.
    # Memory Usage: 15.4 MB, less than 27%.
    # T : O(N), S : O(1)
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        pCnt = [0] * 26  # Count list of chrs in p.
        for ch in p:
            pCnt[ord(ch) - ord("a")] += 1

        sCnt = [0] * 26  # Count list of chrs in first slice of s that is len of p.
        for ch in s[: len(p)]:
            sCnt[ord(ch) - ord("a")] += 1

        res: List[int] = []  # Initilize res list and add index 0 if first slice is anagram.
        if pCnt == sCnt:
            res.append(0)

        # Loop over window of size of p and decremenet left pointer chr
        # and incremenet right point chr. Check if new slice is anagram.
        i = 0
        for j in range(len(p), len(s)):
            sCnt[ord(s[i]) - ord("a")] -= 1
            sCnt[ord(s[j]) - ord("a")] += 1
            if pCnt == sCnt:
                res.append(i + 1)
            i += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert sol.findAnagrams(s="abab", p="ab") == [0, 1, 2]
