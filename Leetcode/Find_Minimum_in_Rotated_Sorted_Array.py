from typing import List


class Solution:
    # Runtime: 73 ms, faster than 31.94% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 24.08% of Python3 online submissions.
    def findMin(nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[-1] > nums[0]:
            # There is no rotation to the sorted array.
            # Array is still sorted.
            return nums[0]

        # There is some rotation.
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            # Check for inflection point, if True :
            # We have found our answer.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # Check for inflection point again. In this case nums is lowest.
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            # Else, if mid > nums[0], that means array is increasing upto nums
            # Search in other half, Rotation will be there.
            if nums[mid] > nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1

        return nums[lo]


sol = Solution()
assert (sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2, 3])) == 0
assert (sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2])) == 0
assert (sol.findMin(nums=[4, 5, 6, 0, 1, 2])) == 0
assert (sol.findMin(nums=[4, 7, 0, 1, 2])) == 0
assert (sol.findMin(nums=[7, 0, 1, 2])) == 0
assert (sol.findMin(nums=[0, 1, 2])) == 0
assert (sol.findMin(nums=[1, 2])) == 1
assert (sol.findMin(nums=[3, 2])) == 2
assert (sol.findMin(nums=[3])) == 3
assert (sol.findMin(nums=[2, 3, 4, 5, 1])) == 1
