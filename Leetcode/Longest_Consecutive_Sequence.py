from typing import List


class Solution:
    # Upoptimal Code. O(NlogN) Time, O(1) space.
    # Runtime: 354 ms, faster than 87.32%
    # Memory Usage: 26.9 MB, less than 91.49%
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        maxCount = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                    maxCount = max(count, maxCount)
                else:
                    count = 1

        return maxCount

    # Runtime: 699 ms, faster than 46.54%
    # Memory Usage: 28.5 MB, less than 42.76%
    # Time complexity : O(n).
    """Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear. Because the while loop is reached only when currentNum marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), the while loop can only run for n iterations throughout the entire runtime of the algorithm. This means that despite looking like O(n x n) complexity, the nested loops actually run in O(n+n) time. All other computations occur in constant time, so the overall runtime is linear.
    Space complexity : O(n).
    In order to set up O(1) containment lookups, we allocate linear space for a hash table to store the O(n) numbers in nums."""

    def longestConsecutiveOptimal(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = set(nums)
        count, maxCount = 1, 1
        for num in numsSet:
            if num - 1 not in numsSet:
                # Will only run while loop for the smallest number in a sequence
                while (num + 1) in numsSet:
                    count += 1
                    maxCount = max(count, maxCount)
                    num += 1
                count = 1

        return maxCount


# Wrong code, nums[i] are in range(-10^9, 10^9)
# Algo : Create array of length max(nums), at index nums[i] put 1, compute on that.
# 7/71 passed
# N = max(nums)
# out = [0] * (N+1)

# for i in nums:
#     out[i] = 1

# count = 1
# maxCount = 1
# for _ in range(len(out) - 1):
#     if out[_]:
#         if out[_ - 1]:
#             count += 1
#             maxCount = max(count, maxCount)
#         else:
#             count = 1
