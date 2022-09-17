from typing import List


class Solution:
    # Runtime: 61 ms, faster than 70.44% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 44.69% of Python3 online submissions.
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            post = mid + 1
            # Follow the slope
            if nums[mid] - nums[post] > 0:
                # if nums[mid] - nums[post] > 0:
                # Downward slope
                # Search in the first half.
                hi = mid
            else:
                # Upward slope
                # Search in the second half.
                lo = mid + 1

        return lo

    def findPeakElementOfficial(self, nums: List[int]) -> int:
        lo = 0
        r = len(nums) - 1
        while lo < r:
            mid = (lo + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                lo = mid + 1

        return lo

    # Runtime: 107 ms, faster than 5.38% of Python3 online submissions for Find Peak Element.
    # Memory Usage: 14 MB, less than 44.69% of Python3 online submissions for Find Peak Element.
    def findPeakElementClean(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            pre = mid - 1
            post = mid + 1
            # Check if mid is the peak or not, it has to be greater than both it neighbours.
            # Or maybe be at the edges.
            if (mid == 0 or nums[pre] < nums[mid]) and (mid == n - 1 or nums[mid] > nums[post]):
                return mid
            elif mid == 0 or nums[mid] - nums[pre] > 0:
                # Upward slope
                # Search in the second half.
                lo = mid + 1
            # elif (mid == n - 1) or nums[mid] - nums[post] > 0:
            else:
                # Downward slope
                # Search in the first half.
                hi = mid - 1

        return lo


sol = Solution()
assert (sol.findPeakElementClean(nums=[1, 2, 1, 3, 5, 6, 4])) in [1, 5]
assert (sol.findPeakElementClean(nums=[1, 2, 3, 1])) in [2]
assert (sol.findPeakElementClean(nums=[1, 2, 1, 3, 5, 6, 4])) in [5]
assert (sol.findPeakElementClean(nums=[1])) in [0]
assert (sol.findPeakElementClean(nums=[1, 2])) in [1]
