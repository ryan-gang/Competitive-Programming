from bisect import bisect_left
from typing import List


class Solution:
    # Runtime: 58 ms, faster than 83.66% of Python3 online submissions.
    # Memory Usage: 14.7 MB, less than 83.19% of Python3 online submissions.
    # T : O(lgN), S : O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return lo

    def searchInsert1(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


if __name__ == "__main__":
    sol = Solution()
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
    assert sol.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
