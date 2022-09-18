class Solution:
    # Runtime: 61 ms, faster than 31.28% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 43.02% of Python3 online submissions.
    # T : O(N), S : O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        m, n = len(s), len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == m

    # Ref : https://leetcode.com/problems/is-subsequence
    # /discuss/87258/2-lines-Python
    """Iter helps make sure, the checking is done sequentially, if iter() is not used,
    order will be ignored. Because of iter() order is taken into consideration."""
    def isSubsequence1L(self, s, t):
        t = iter(t)
        return all(c in t for c in s)


sol = Solution()
assert sol.isSubsequence(s="abc", t="ahbgdc")
assert not sol.isSubsequence(s="axc", t="ahbgdc")
