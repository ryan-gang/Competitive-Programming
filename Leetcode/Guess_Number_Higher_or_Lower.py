class Solution:
    @staticmethod
    def guess(num: int) -> int:
        NUMBER = 69
        return num > NUMBER

    # Runtime: 32 ms, faster than 92.65% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 66.11% of Python3 online submissions.
    def guessNumber(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            g = Solution.guess(mid)
            if g < 0:
                hi = mid - 1
            elif g > 0:
                lo = mid + 1
            else:
                return mid
        return lo
