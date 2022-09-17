from typing import List


class Solution:
    # Runtime: 1287 ms, faster than 54.32% of Python3 online submissions.
    # Memory Usage: 18.1 MB, less than 72.13% of Python3 online submissions.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        n = len(nums)
        for lo in range(0, n - 2):
            mid = lo + 1
            hi = n - 1
            target = 0 - nums[lo]
            if lo > 0 and nums[lo] == nums[lo - 1]:
                continue
            while mid < hi:
                added_value = nums[mid] + nums[hi]
                if added_value == target:
                    out.append([nums[lo], nums[mid], nums[hi]])
                    while mid < hi and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    mid += 1
                    hi -= 1
                elif added_value > target:
                    hi -= 1
                else:
                    mid += 1

        return out


sol = Solution()
assert sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert sol.threeSum(nums=[0, 1, 1]) == []
assert sol.threeSum(nums=[0, 0, 0]) == [[0, 0, 0]]
