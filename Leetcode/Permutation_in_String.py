class Solution:
    # Runtime: 84 ms, faster than 85.07% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 31.78% of Python3 online submissions.
    # T : O(l1 + 26*(l2 - l1)), S : O(1)
    # T : O(l1) to create the array1, and then l2 - l1 iterations, comparing arrays of length 26.
    # Space is still not optimal, instead of comparing entire arrays
    # in every iteration, try to compare the changes.
    # TODO https://leetcode.com/problems/permutation-in-string/solution/
    def checkInclusion(self, s1: str, s2: str) -> bool:
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


sol = Solution()
assert sol.checkInclusion(s1="ab", s2="eidbaooo")
assert not (sol.checkInclusion(s1="ab", s2="eidboaoo"))
assert sol.checkInclusion(s1="a", s2="ab")
assert sol.checkInclusion(s1="adc", s2="dcda")
assert not sol.checkInclusion(s1="ab", s2="a")
