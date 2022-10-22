from collections import Counter, defaultdict
from typing import Dict


# Runtime: 1470 ms, faster than 5.00% of Python3 online submissions.
# Memory Usage: 14.7 MB, less than 36.77% of Python3 online submissions.
# T : O(S*T), S : O(S+T)
# For every iteration, checking against all the keys in t, if dicts match.
class Solution:
    @staticmethod
    def compare_dict(large: Dict[str, int], small: Dict[str, int]) -> bool:
        """Return true if large contains all keys from small, and equal to or greater values"""
        for key in small:
            if key in large:
                if large[key] < small[key]:
                    return False
            else:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        lo, hi, n, min_window = 0, 0, len(s), float("inf")
        ans = ""
        ds = defaultdict(int)
        dt = Counter(t)

        if t == "" or len(t) > len(s):
            return ans

        while hi < n:
            ds[s[hi]] += 1
            hi += 1
            while Solution.compare_dict(ds, dt):
                if (hi - lo) < min_window:
                    ans = s[lo:hi]
                    min_window = hi - lo
                ds[s[lo]] -= 1
                lo += 1

        return ans

    # Leetcode Editorial.
    # T : O(S + T), S : O(S + T)
    # Instead of checking entire dict every time, keep iteratively checking in every iteration.
    # Keep a count of matching chars, and the number of matches we require, update this regularly.
    def minWindow2(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        left, right = 0, 0

        # formed is used to keep track of how many unique characters in t are
        # present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C.
        # Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), -1, -1

        while right < len(s):

            # Add one character from the right to the window
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired
            # count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while left <= right and formed == required:
                character = s[left]

                # Save the smallest window until now.
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # The character at the position pointed by the `left` pointer is
                # no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                left += 1

            # Keep expanding the window once we are done contracting.
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow(s="ANBXYZXYZCABN", t="ABC") == "CAB"
    assert sol.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert sol.minWindow(s="a", t="a") == "a"
    assert sol.minWindow(s="a", t="aa") == ""
    assert sol.minWindow(s="cabwefgewcwaefgcf", t="cae") == "cwae"
