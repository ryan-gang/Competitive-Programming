from typing import List


class Solution:
    """50/75 TC passed. Wrong answer.
    Breaks down for [1,2,1,1]
    The idea was, as we can rob atmost one out of the first and the last house,
    so we find the max, and store it in the first cell, and remove the last cell.
    But the problem with that logic is we are altering the structure of the nums,
    which will inevitably break the solution."""

    def robWrong(self, nums: List[int]) -> int:
        nums[0] = max(nums[0], nums[-1])
        if len(nums) == 1:
            return nums[0]
        nums = nums[:-1]
        prevprev = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = max(prev, prevprev + nums[i])
            prevprev, prev = prev, curr
        return prev

    """Now, what we have here is circular pattern.
    Imagine, that we have 10 houses: a0, a1, a2, a3, ... a9: Then we have two possible options:
    Rob house a0, then we can not rob a1 or a9 and we have a2, a3, ..., a8 range to rob
    Do not rob house a0, then we have a1, a2, ... a9 range to rob.
    Then we just choose maximum of these two options and we are done!"""
    # Runtime: 61 ms, faster than 22.76% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 23.90% of Python3 online submissions.
    # T : O(N), S : O(1)
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            if not nums:
                return 0
            prevprev, prev = 0, nums[0]
            for i in range(1, len(nums)):
                curr = max(prev, prevprev + nums[i])
                prevprev, prev = prev, curr
            return prev

        """We could have done :
        max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
        But in that case, if len(nums) == 1, we will need to have a separate case to return nums[0].
        Because both times helper is called with a []. So to handle that edge case
        gracefully, we are doing nums[0] + rob_helper(nums[2:-1]) instead of rob_helper(nums[:-1])
        So this also acceptable :
        if len(nums) == 1: return nums[0]
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))
        """
        return max(nums[0] + rob_helper(nums[2:-1]), rob_helper(nums[1:]))


sol = Solution()
assert sol.rob(nums=[7, 1, 1, 7]) == 8
assert sol.rob(nums=[2, 3, 2]) == 3
assert sol.rob(nums=[1, 2, 3, 1]) == 4
assert sol.rob(nums=[1, 2, 3]) == 3
assert sol.rob(nums=[1, 2, 1, 1]) == 3
assert sol.rob(nums=[1]) == 1
