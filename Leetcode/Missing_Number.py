from typing import List


class Solution:
    # 1. Sorting linear search
    def missingNumberSLS(nums):
        nums.sort()
        for _ in range(len(nums)):
            if _ != nums[_]:
                return _

    # 2. Sorting binary search
    def missingNumberSBS(nums):
        nums.sort()
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    """
    As the numbers are in range [0, N], their indices are also in range [0, N],
    and we know one of them is missing.
    So if we XOR all the indices and their values,
    we will find the missing number.
    a ^ a = 0
    """
    # Runtime: 137 ms, faster than 95.84% of Python3 online submissions.
    # Memory Usage: 15.2 MB, less than 40.22% of Python3 online submissions.
    def missingNumberBitManipulate(nums):
        out = len(nums)  # This index will not be present in nums, so init value.
        for idx, val in enumerate(nums):
            out ^= idx ^ val

        return out

    # Difference between sum of 0 to N using formula, and actual sum.
    def missingNumberSum(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)
