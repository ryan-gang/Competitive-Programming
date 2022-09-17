from typing import List


class Solution:
    # Runtime: 251 ms, faster than 94.37% of Python3 online submissions.
    # Memory Usage: 15.4 MB, less than 97.68% of Python3 online submissions.
    # T : O(lgN), S : O(1)
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1


sol = Solution()
assert sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
