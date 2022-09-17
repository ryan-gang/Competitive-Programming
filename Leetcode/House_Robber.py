from typing import List


class Solution:
    # Runtime: 47 ms, faster than 58.27% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 19.71% of Python3 online submissions.
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1] = nums[0]
        for i in range(1, n):
            dp[i + 1] = max((dp[i - 1] + nums[i]), dp[i])

        return dp[-1]

    # Runtime: 66 ms, faster than 11.83% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 97.22% of Python3 online submissions.
    # Next challenges:
    # T : O(N), S : O(N)
    def rob2(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1]) # Is covered by i = 1.
        for i in range(1, len(nums)):
            # ith cell's max possible value (loot) will be either i - 1th cell's loot,
            # or i - 2th cell's loot + ith cell.
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # Runtime: 72 ms, faster than 5.63% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 19.67% of Python3 online submissions.
    # T : O(N), S : O(1)
    def rob3(self, nums):
        prevprev = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = max(prev, prevprev + nums[i])
            prevprev, prev = prev, curr
        return prev


sol = Solution()
assert sol.rob3(nums=[7, 1, 1, 7]) == 14
assert sol.rob3(nums=[1, 2, 3, 1]) == 4
assert sol.rob3(nums=[2, 7, 9, 3, 1]) == 12
assert sol.rob3(nums=[1, 2, 3]) == 4
assert sol.rob3(nums=[0]) == 0
