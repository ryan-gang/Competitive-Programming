import math


class Solution:
    def __init__(self) -> None:
        self.all_powers = set()
        count, val = 0, 1
        # Why 21 ? Max number is 2 ^ 32,
        # Let 2 ^ 32 == 3 ^ x
        # x = math.log(2)/math.log(3) * 32
        while count < 21:
            self.all_powers.add(val)
            val *= 3
            count += 1

    # Runtime: 239 ms, faster than 9.86% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions.
    def isPowerOfThreeSet(self, n: int) -> bool:
        return n in self.all_powers

    # Runtime: 91 ms, faster than 87.36% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 57.97% of Python3 online submissions.
    def isPowerOfThreeIter(self, n: int) -> bool:
        while n >= 1:
            if n == 1:
                return True
            else:
                n /= 3

    # BROKEN.
    # logn gives randomly super close values.
    def isPowerOfThreeMath(self, n: int) -> bool:
        # n = 3 ^ x, log n = x log 3
        # x = log n / log 3
        epsilon = 0.000001
        if n <= 0:
            return False
        x = math.log(n) / math.log(3) + epsilon
        return abs(x - int(x)) <= 2 * epsilon

    # Runtime: 126 ms, faster than 58.41% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions.
    def isPowerOfThreeMathClean(self, n: int) -> bool:
        # n = 3 ^ x, log n = x log 3
        # x = log n / log 3
        if n <= 0:
            return False
        x = math.log10(n) / math.log10(3)
        return not (int(x) - x)


sol = Solution()
print(sol.isPowerOfThreeMath(27))
