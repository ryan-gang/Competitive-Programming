from typing import List


class Solution:
    # Runtime: 296 ms, faster than 24.64% of Python3 online submissions.
    # Memory Usage: 15.3 MB, less than 11.07% of Python3 online submissions.
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = nums[:]
        right = nums[:]
        # Create running sum array starting from the left, and starting from the right.
        # Also called prefix sum array.
        for i in range(1, n):
            left[i] += left[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] += right[i + 1]

        # Check if pivot is 0.
        try:
            if right[1] == 0:
                return 0
        except IndexError:
            pass

        # Iterate pivot from 1 to n - 2,
        # at every iteration, check if the prefix sum arrays match.
        for pivot in range(1, n - 1):
            left_sum = left[pivot - 1]
            right_sum = right[pivot + 1]
            if left_sum == right_sum:
                return pivot
        # Check if pivot is n - 1
        try:
            if left[n - 2] == 0:
                return n - 1
        except IndexError:
            pass

        return -1

    # My solution is needlessly chaotic, this is much better and clean.
    def pivotIndexClean(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1


sol = Solution()
assert sol.pivotIndexClean(nums=[1, 7, 3, 6, 5, 6]) == 3
assert sol.pivotIndexClean(nums=[1, 2, 3]) == -1
assert sol.pivotIndexClean(nums=[1, 2, 1]) == 1
assert sol.pivotIndexClean(nums=[2, 1, -1]) == 0
assert sol.pivotIndexClean(nums=[1]) == -1
assert sol.pivotIndexClean(nums=[1, 1]) == -1
assert sol.pivotIndexClean(nums=[-1, -1, 0, 1, 1, -1]) == 0
assert sol.pivotIndexClean(nums=[-1, -1, 0, 1, 1, 0]) == 5
