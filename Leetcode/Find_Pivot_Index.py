from typing import List


class Solution:
    """
    First attempt, ignore this solution."""

    # Runtime: 296 ms, faster than 24.64% of Python3 online submissions.
    # Memory Usage: 15.3 MB, less than 11.07% of Python3 online submissions.
    def pivotIndexChaos(self, nums: List[int]) -> int:
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
    def pivotIndexClean(self, nums: list[int]):
        S = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i
            left_sum += x
        return -1

    """
    Initially prefix_sum = 0 and suffix_sum = sum(nums).
    For every index in nums, first remove that from suffix_sum. (At this point none of prefix_sum
    or suffix_sum contain the ith index.) Now compare if the sums are equal.
    Then after the comparison add the ith index to the prefix_sum for the next iteration."""
    # Runtime: 157 ms, faster than 93.91% of Python3 online submissions.
    # Memory Usage: 15.3 MB, less than 11.31% of Python3 online submissions.
    def pivotIndexElegant(self, nums: List[int]) -> int:
        suffix_sum = sum(nums)
        prefix_sum = 0
        for i, v in enumerate(nums):
            suffix_sum -= v
            if prefix_sum == suffix_sum:
                return i
            prefix_sum += v
        return -1

    # Runtime: 506 ms, faster than 19.39%.
    # Memory Usage: 15 MB, less than 99.39%.
    # T : O(N), S : O(N)
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums) - nums[0]
        idx = 1
        while idx < len(nums) and left_sum != right_sum:
            left_sum += nums[idx - 1]
            right_sum -= nums[idx]
            idx += 1

        return idx - 1 if left_sum == right_sum else -1


sol = Solution()
assert sol.pivotIndex(nums=[1, 7, 3, 6, 5, 6]) == 3
assert sol.pivotIndex(nums=[1, 2, 3]) == -1
assert sol.pivotIndex(nums=[1, 2, 1]) == 1
assert sol.pivotIndex(nums=[2, 1, -1]) == 0
assert sol.pivotIndex(nums=[1]) == 0
assert sol.pivotIndex(nums=[1, 1]) == -1
assert sol.pivotIndex(nums=[-1, -1, 0, 1, 1, -1]) == 0
assert sol.pivotIndex(nums=[-1, -1, 0, 1, 1, 0]) == 5
