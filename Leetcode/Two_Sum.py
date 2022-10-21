from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, b in enumerate(nums):
            a = target - b
            if a in seen:
                return [seen[a], i]
            seen[b] = i

        return []

    # Binary Search on sorted d.items()
    # Not sure how it is supposed to save time.
    # Creating dict/list O(N), sorting O(NlogN), Binary Search O(logN)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()  # Sort arr in increasing order by their values.

        left, right = 0, len(arr) - 1
        while left < right:
            sum_ = arr[left][0] + arr[right][0]
            if sum_ == target:
                return [arr[left][1], arr[right][1]]
            elif sum_ > target:
                right -= 1  # Try to decrease sum_
            else:
                left += 1  # Try to increase sum_

        return []
