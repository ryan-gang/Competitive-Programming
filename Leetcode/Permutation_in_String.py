from collections import Counter


class Solution:
    # Runtime: 84 ms, faster than 85.07% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 31.78% of Python3 online submissions.
    # T : O(l1 + 26*(l2 - l1)), S : O(1)
    # T : O(l1) to create the array1, and then l2 - l1 iterations, comparing arrays of length 26.
    # Time is still not optimal, instead of comparing entire arrays
    # in every iteration, try to compare the changes.
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        array1 = [0 for _ in range(26)]
        array2 = [0 for _ in range(26)]

        window_size = len(s1)
        for i in range(window_size):
            array1[ord(s1[i]) - ord("a")] += 1
            array2[ord(s2[i]) - ord("a")] += 1

        for lo in range(len(s2) - window_size):
            if array1 == array2:
                return True
            hi = lo + window_size
            array2[ord(s2[lo]) - ord("a")] -= 1
            array2[ord(s2[hi]) - ord("a")] += 1

        return array1 == array2

    # Runtime: 167 ms, faster than 50.93% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 6.72% of Python3 online submissions.
    # T : O(L1 + (L2 - L1)), S : O(1)
    # Instead of comparing the entire array we are comparing only the changed indices.
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        array1 = [0 for _ in range(26)]
        array2 = [0 for _ in range(26)]

        window_size = len(s1)
        for i in range(window_size):
            array1[ord(s1[i]) - ord("a")] += 1
            array2[ord(s2[i]) - ord("a")] += 1

        count = 0
        for i in range(26):
            if array1[i] == array2[i]:
                count += 1

        if count == 26:
            return True

        for lo in range(len(s2) - window_size):
            hi = lo + window_size
            lo_idx, hi_idx = ord(s2[lo]) - ord("a"), ord(s2[hi]) - ord("a")
            array2[lo_idx] -= 1
            array2[hi_idx] += 1

            if hi_idx != lo_idx:
                # If the leaving and entering char are same, no need to do any computation,
                # everything remains the same.
                if array2[lo_idx] == array1[lo_idx]:
                    # They are now same, after the update.
                    count += 1
                elif array2[lo_idx] == (array1[lo_idx] - 1):
                    # They were previously same, before the update.
                    count -= 1

                if array2[hi_idx] == array1[hi_idx]:
                    count += 1
                elif array2[hi_idx] == (array1[hi_idx] + 1):
                    count -= 1
            if count == 26:
                return True

        return count == 26

    # Runtime: 109 ms, faster than 55.15%.
    # Memory Usage: 13.9 MB, less than 94.40%.
    # T : O(L1 + 26(L2 - L1)), S : O(1) (26 keys. Constant.)
    # Creating hashmap for s1 -> l1, for s2 -> l1. (same length).
    # Then for l2 - l1 chars in s2, we do a comparison between 2 dicts.
    # O(26) keys at most.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Compare rolling counters of 2 strings, (same window sizes.)
        lo, hi = 0, len(s1)
        d1 = Counter(s1)
        d2 = Counter(s2[:hi])

        if d1 == d2:
            return True

        while hi < len(s2):
            d2[s2[lo]] -= 1
            d2[s2[hi]] += 1
            if d1 == d2:
                return True
            lo += 1
            hi += 1

        return d1 == d2


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion(s1="ab", s2="eidbaooo")
    assert not sol.checkInclusion(s1="ab", s2="eidboaoo")
    assert sol.checkInclusion(s1="a", s2="ab")
    assert sol.checkInclusion(s1="adc", s2="dcda")
    assert not sol.checkInclusion(s1="ab", s2="a")
    assert sol.checkInclusion(
        s1="trinitrophenylmethylnitramine", s2="dinitrophenylhydrazinetrinitrophenylmethylnitramine"
    )
    assert not sol.checkInclusion(s1="abd", s2="abcabe")
