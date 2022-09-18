from typing import List


class Solution:
    # Runtime: 43 ms, faster than 82.81% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 27.03% of Python3 online submissions.
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        runningSum = 0
        for num in nums:
            runningSum += num
            out.append(runningSum)

        return out

    # Runtime: 35 ms, faster than 97.54% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 73.38% of Python3 online submissions.
    def runningSumInPlace(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums
