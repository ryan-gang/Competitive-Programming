from typing import List


class Solution:
    """
    dp[i] is the number of "arithmetic subarrays" ending at the ith index.
    dp[i + 1] can be calculated as dp[i] + 1
    Because all the X (X = dp[i]) subarrays, are also valid for i+1 th index,
    We can just add the i+1th element to the subarrays.
    But along with that we also gain a NEW subarray, which was previously invalid
    (was of length 2, now is of lenght 3 and is valid)
    """

    # Runtime: 75 ms, faster than 18.73% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 12.46% of Python3 online submissions.
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = dp[1] = 0  # No valid subarrays (of length >= 3) end at 0th or 1st index.
        for i in range(2, len(nums)):
            # Check if element at current index (i) is valid.
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                pass

        print(dp)
        return sum(dp)


sol = Solution()
assert sol.numberOfArithmeticSlices(nums=[1, 2, 3, 4]) == 3
assert sol.numberOfArithmeticSlices(nums=[1]) == 0
assert sol.numberOfArithmeticSlices(nums=[1, 2, 3, 4, 9, 11, 13, 15]) == 6
