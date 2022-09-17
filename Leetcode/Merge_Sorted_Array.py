from typing import List


# Runtime: 32 ms, faster than 97.78% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14 MB, less than 37.34% of Python3 online submissions for Merge Sorted Array.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        j += 1
        if j > 0:
            nums1[:j] = nums2[:j]
