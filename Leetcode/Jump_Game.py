from typing import List


class Solution:
    # Runtime: 1356 ms, faster than 13.07% of Python3 online submissions.
    # Memory Usage: 15.1 MB, less than 96.73% of Python3 online submissions.
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [0 for _ in range(n)]
        for i in range(0, n - 1):
            tmp = max(dp[i - 1] - 1, nums[i])
            if tmp < 1:
                return False
            dp[i] = tmp

        print(dp)
        return True


sol = Solution()
assert sol.canJump(nums=[2, 3, 1, 1, 4])
assert not sol.canJump(nums=[3, 2, 1, 0, 4])
assert sol.canJump(nums=[0])
assert not sol.canJump(nums=[0, 2, 3])
assert sol.canJump(nums=[2, 0, 0])
