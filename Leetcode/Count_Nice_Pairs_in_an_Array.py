from collections import Counter, defaultdict
from math import factorial


class Solution:
    def rev(self, x: int) -> int:
        return int(str(x)[::-1])

    def nCr(self, n: int, r: int):
        return int(factorial(n) / (factorial(r) * factorial(n - r)))

    def countNicePairs(self, nums: list[int]) -> int:
        for idx, val in enumerate(nums):
            nums[idx] = val - self.rev(val)

        d = Counter(nums)
        values = d.values()
        total = 0
        # Of all the elements appearing twice or more, we can create nC2 pairs.
        # We count all the pairs possible in the total.
        for val in values:
            if val > 1:
                total += self.nCr(val, 2)

        return total % (10**9 + 7)

    def countNicePairs1(self, nums: list[int]) -> int:
        d: dict[int, int] = defaultdict(int)
        total = 0
        for val in nums:
            new = val - self.rev(val)
            # Till now we have seen x dupes of new, we can create x new pairs,
            # we add x to the total, and increment x. This is repeated for every
            # collision.
            total += d[new]
            d[new] += 1
        return total % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()
    assert sol.countNicePairs(nums=[13, 10, 35, 24, 76]) == 4
    assert sol.countNicePairs(nums=[1, 10]) == 0
