import sys
from bisect import bisect_left
from typing import List


class Solution:
    # Ref : https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
    # Runtime: 8370 ms, faster than 25.62% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 53.95% of Python3 online submissions.
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Fix one index, and then use two pointers on the rest of the array, to reach
        closer to target."""

        nums.sort()
        n = len(nums) - 1
        result: int = sys.maxsize  # Or math.inf Or float('inf')
        for i in range(n - 1):
            j, k = i + 1, n
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == target:
                    return val
                elif abs(target - val) < abs(target - result):
                    result = val

                if val > target:
                    k -= 1
                elif val < target:
                    j += 1

        return result

    # Runtime: 361 ms, faster than 96.45% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 12.36% of Python3 online submissions.
    def threeSumClosestBinS(self, nums: List[int], target: int) -> int:
        """Instead of the normal 2 pointer technique, to reach ever closer to target,
        we use Binary Search here, as the array is already sorted, it's just a matter of
        implementation."""

        nums.sort()
        best = sys.maxsize

        # The window is: [i, j, k]
        # Valid range for i:
        for i in range(0, len(nums) - 2):
            # Instead of incrementaly updating the k and j,
            # we can use binary search to find the next viable value for each.
            # We pingpong between updating j and k
            pingpong = 0

            # Pick a j (k will be overriden on first pass)
            j = i + 1
            k = len(nums)

            while k > i + 2:
                if pingpong % 2 == 0:
                    # Decrease k until sum can be less than target
                    targetVal = target - nums[i] - nums[j]
                    newj = bisect_left(nums, targetVal, j + 1, k - 1)
                    # There is no possible update to k, can stop
                    # searching
                    if newj == k:
                        break
                    k = newj
                    pingpong += 1
                else:
                    # Increase j until sum can exceed target
                    targetVal = target - nums[i] - nums[k]
                    j = bisect_left(nums, targetVal, i + 1, k - 1)
                    if nums[j] > targetVal and j > i + 1:
                        j -= 1
                    pingpong += 1

                new = nums[i] + nums[j] + nums[k]
                if abs(best - target) > abs(target - new):
                    best = new

                if best == target:
                    return target

        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2
    assert sol.threeSumClosest(nums=[0, 0, 0], target=1) == 0
