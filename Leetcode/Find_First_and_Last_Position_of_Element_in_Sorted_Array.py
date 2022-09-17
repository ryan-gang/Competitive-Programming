from typing import List


class Solution:
    # Runtime: 117 ms, faster than 62.75% of Python3 online submissions.
    # Memory Usage: 15.5 MB, less than 50.23% of Python3 online submissions.
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lo, hi = 0, n - 1
        out = []

        # If nums is empty, return out.
        if not nums:
            return [-1, -1]

        # This code block will find the starting index of target.
        # Which is achieved by searching for mid, such that nums[mid] is target
        # but the previous element is not target.
        # As a result if target is our first element,
        # this block will not pick it up, so we handle it seperately.
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target and mid >= 1 and nums[mid - 1] != target:
                out.append(mid)
                break
            elif nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        # If target is present, and it is not the 0th element,
        # it should have been added to out by now.
        # If it is not there, that means either it is absent
        # Or it is the starting element.
        # Accordingly we add the index or -1 to out.
        if len(out) < 1:
            if nums[0] == target:
                out.append(0)
            else:
                out.append(-1)

        # This code block searches for the last index of target
        # Using a similar philosophy as our previous code block
        # nums[mid] == target but nums[mid + 1] is not target
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target and mid <= n - 2 and nums[mid + 1] != target:
                out.append(mid)
                break
            elif nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1

        # And accordingly we handle edge cases.
        if len(out) < 2:
            if nums[-1] == target:
                out.append(n - 1)
            else:
                out.append(-1)

        return out

    # 95 ms, faster than 87.05% of Python3 online submissions.
    # Memory Usage: 15.4 MB, less than 48.44% of Python3 online submissions.
    def searchRangeClean(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n = len(nums)
        lo, hi, index = 0, n - 1, None
        # Here, our philosophy is different, we find target. Any index of target.
        # Then go on decreasing left index until we find the left edge of target.
        # And similarly the right edge.
        # This code is suboptimal to the previous one,
        # if the target is repeated hundreds of times. We will run a loop for that many iterations.
        # So, binary search to find both the edges is optimal. 
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] >= target:
                hi = mid - 1
            else:
                lo += 1
        # If target is in nums, index will be defined here, else return [-1, -1]
        if index is None:
            return [-1, -1]
        lo = hi = index
        while lo >= 0 and nums[lo] == target:
            lo -= 1
        lo += 1
        while hi < len(nums) and nums[hi] == target:
            hi += 1
        hi -= 1

        return [lo, hi]


sol = Solution()
print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(sol.searchRange(nums=[], target=0))
print(sol.searchRange(nums=[1], target=1))
