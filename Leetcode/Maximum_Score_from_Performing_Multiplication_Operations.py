from functools import lru_cache
from typing import List
from StarterCode.decorators import timeit


class Solution:
    def maximumScoreGreedyNaieve(self, nums: List[int], multiplier: List[int]) -> int:
        n = len(multiplier)
        dp = [0 for _ in range(n)]
        if multiplier[0] * nums[0] > multiplier[0] * nums[n - 1]:
            dp[0] = [multiplier[0] * nums[0], 1, n - 1]
        else:
            dp[0] = [multiplier[0] * nums[n - 1], 0, n - 2]

        for i in range(1, n):
            prev, start, end = dp[i - 1]
            a = (multiplier[i] * nums[start]) + prev
            b = (multiplier[i] * nums[end]) + prev
            if a > b:
                dp[i] = [a, start + 1, end]
            else:
                dp[i] = [b, start, end - 1]

        return dp[-1][0]

    @timeit
    # 43 / 50 TC passed. TLE.
    # Even with lru_cache, the helper could run on 2^N cases.
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Number of Operations
        m = len(multipliers)

        @lru_cache(maxsize=None)
        def helper(left, right, op):
            if op == m:
                return 0
            return max(
                nums[left] * multipliers[op] + helper(left + 1, right, op + 1),
                nums[right] * multipliers[op] + helper(left, right - 1, op + 1),
            )

        return helper(0, len(nums) - 1, 0)


sol = Solution()
assert sol.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]) == 102
