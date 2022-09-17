from typing import List


class Solution:
    # When sum == target is required.
    def minSubArrayLenExactTarget(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        lo, hi, sum = 0, 0, 0
        while lo < len(nums):
            if sum < target:
                if hi >= len(nums):
                    break
                sum += nums[hi]
                hi += 1
            elif sum > target:
                sum -= nums[lo]
                lo += 1
            else:
                # print(sum)
                # print(lo, hi - 1)
                window_size = (hi - 1) - lo + 1
                min_size = min(min_size, window_size)
                sum -= nums[lo]
                lo += 1

        if min_size == float("inf"):
            return 0
        return min_size

    # Runtime: 443 ms, faster than 36.47% of Python3 online submissions.
    # Memory Usage: 27.1 MB, less than 42.23% of Python3 online submissions.
    def minSubArrayLenSW(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        lo, hi, sum = 0, 0, 0
        while lo < len(nums):
            if sum < target:
                if hi >= len(nums):
                    break
                sum += nums[hi]
                hi += 1
            elif sum >= target:
                # print(sum)
                # print(lo, hi - 1)
                window_size = (hi - 1) - lo + 1
                min_size = min(min_size, window_size)
                sum -= nums[lo]
                lo += 1

        if min_size == float("inf"):
            return 0
        return min_size

    # Runtime: 830 ms, faster than 5.02% of Python3 online submissions.
    # Memory Usage: 27.1 MB, less than 86.86% of Python3 online submissions.
    def minSubArrayLenClean(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        lo, sum = 0, 0
        for hi in range(len(nums)):
            sum += nums[hi]
            while sum >= target:
                window_size = (hi) - lo + 1
                min_size = min(min_size, window_size)
                sum -= nums[lo]
                lo += 1

        return min_size if min_size < float("inf") else 0


sol = Solution()
print(sol.minSubArrayLenClean(target=7, nums=[2, 3, 1, 2, 4, 3]))
assert sol.minSubArrayLenClean(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
assert sol.minSubArrayLenClean(target=4, nums=[1, 4, 4]) == 1
assert sol.minSubArrayLenClean(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert sol.minSubArrayLenClean(target=11, nums=[1, 2, 3, 4, 5]) == 3
