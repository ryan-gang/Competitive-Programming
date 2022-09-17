s = "MCMXCIV"
s = "LVIII"
s = "III"
s = "MCMXCVI"


class Solution:
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Runtime: 61 ms, faster than 74.52%.
    # Memory Usage: 13.9 MB, less than 76.17%.
    def romanToInt1(self, s: str) -> int:
        val = Solution.mapping[s[-1]]
        for i in range(len(s) - 1):
            if Solution.mapping[s[i]] < Solution.mapping[s[i + 1]]:
                val -= Solution.mapping[s[i]]
            else:
                val += Solution.mapping[s[i]]

        return val

    # Runtime: 79 ms, faster than 47.11% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 76.66% of Python3 online submissions.
    # T : O(N), S : O(1)
    def romanToInt(self, s: str) -> int:
        # The while loop will only go upto len(s) - 1, so the last char will be not processed.
        # So adding it initially.
        int_value = Solution.mapping[s[-1]]
        lo = 0
        while lo < len(s) - 1:
            hi = lo + 1
            if Solution.mapping[s[lo]] >= Solution.mapping[s[hi]]:
                int_value += Solution.mapping[s[lo]]
            else:
                int_value -= Solution.mapping[s[lo]]
            lo += 1
        return int_value


sol = Solution()
print(sol.romanToInt(s="LVIII"))
assert (sol.romanToInt(s="III")) == 3
assert (sol.romanToInt(s="LVIII")) == 58
assert (sol.romanToInt(s="MCMXCIV")) == 1994
assert (sol.romanToInt(s="MCMXCVI")) == 1996
