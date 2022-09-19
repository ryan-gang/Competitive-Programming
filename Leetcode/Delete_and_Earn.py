from collections import Counter
from typing import List


class Solution:
    """
    dp[i] stands for the max sum we can obtain by "taking" ith element.
    There are 2 possibilities : we can either take the ith number, or pass over it.
    1. If we take it. Our total will be dp[i-2] + nums[i]
    2. We can pass over it. Our total will be dp[i-1]
    For dp[i] we need to take the max of the 2 possibilites.
    """

    # Runtime: 176 ms, faster than 32.71% of Python3 online submissions.
    # Memory Usage: 16 MB, less than 60.57% of Python3 online submissions.
    # T : O(M), S : O(M) (M = max(nums))
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = max(nums) + 1
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max(dp[i - 1], dp[i - 2] + (d[i] * i))
        return dp[-1]

    # Reduced space usage. No dp array required.
    def deleteAndEarnOptimised(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = max(nums) + 1
        skipi = takei = skipprev = takeprev = 0
        for i in range(n):
            # If we decide to take i, we need to use the value we got by skipping i-1.
            takei = skipprev + (i * d[i])
            # If we decide to skip i, state @ i will be the max of skip i -1 and take i - 1.
            skipi = max(skipprev, takeprev)
            skipprev, takeprev = skipi, takei
        return max(skipi, takei)


sol = Solution()
assert sol.deleteAndEarnOptimised(nums=[2, 2, 3, 3, 3, 4]) == 9
assert sol.deleteAndEarnOptimised(nums=[2, 2, 2, 3, 3, 3, 4]) == 10
assert sol.deleteAndEarnOptimised(nums=[2, 2, 2, 4]) == 10
assert sol.deleteAndEarnOptimised(nums=[2, 2, 2, 11, 4]) == 21
assert sol.deleteAndEarnOptimised(nums=[3, 4, 2]) == 6
assert sol.deleteAndEarnOptimised(nums=[1, 1, 1, 2, 4, 5, 5, 5, 6]) == 18
assert sol.deleteAndEarnOptimised(nums=[8, 10, 4, 9, 1, 3, 5, 9, 4, 10]) == 37
