class Solution:
    # Runtime: 41 ms, faster than 86.86%.
    # Memory Usage: 13.8 MB, less than 61.81%.
    def trailingZeroes(self, n: int) -> int:
        """
        Find out the total number of 2's in the factorial, and the total number of 5's.
        As we require both for a 10, we are constrained by the min of the two counts.
        """
        twos, fives = 0, 0
        val = 2
        while n / val >= 1:
            twos += int(n / val)
            val *= 2

        val = 5
        while n / val >= 1:
            fives += int(n / val)
            val *= 5

        return min(twos, fives)


if __name__ == "__main__":
    sol = Solution()
    assert sol.trailingZeroes(n=999) == 246
    assert sol.trailingZeroes(n=0) == 0
    assert sol.trailingZeroes(n=5) == 1
    assert sol.trailingZeroes(n=3) == 0
