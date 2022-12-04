import sys
from typing import List


class Solution:
    # Runtime: 3142 ms, faster than 11.90%.
    # Memory Usage: 24.9 MB, less than 80.12%.
    # T : O(N), S : O(1)
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total, n, idx = sum(nums), len(nums), 0
        left_val, right_val = 0, 0
        avg_diff = 0
        min_avg_diff = (sys.maxsize, 0)

        while idx < n:
            left, right = idx + 1, n - idx - 1
            left_val += nums[idx]
            right_val = total - left_val
            left_avg = left_val // left if left > 0 else 0
            right_avg = right_val // right if right > 0 else 0
            avg_diff = abs(left_avg - right_avg)
            if avg_diff < min_avg_diff[0]:
                min_avg_diff = (avg_diff, idx)
            idx += 1

        return min_avg_diff[1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumAverageDifference(nums=[2, 5, 3, 9, 5, 3]) == 3
    assert sol.minimumAverageDifference(nums=[]) == 0
    assert sol.minimumAverageDifference(nums=[0]) == 0
    assert sol.minimumAverageDifference(nums=[0, 0, 0, 0, 0]) == 0
