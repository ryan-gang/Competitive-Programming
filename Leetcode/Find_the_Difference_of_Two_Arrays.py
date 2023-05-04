class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]
