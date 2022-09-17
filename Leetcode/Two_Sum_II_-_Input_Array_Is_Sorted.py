from typing import List


class Solution:
    # Runtime: 120 ms, faster than 99.64% of Python3 online submissions.
    # Memory Usage: 14.9 MB, less than 88.68% of Python3 online submissions.
    # T : O(N), S : O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo <= hi:
            current_sum = numbers[lo] + numbers[hi]
            if current_sum == target:
                return [lo + 1, hi + 1]
            elif current_sum > target:
                # reduce sum, hi has to come down.
                hi -= 1
            else:
                # increase sum, increase lo.
                lo += 1


sol = Solution()
sol.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
sol.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
sol.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
sol.twoSum(numbers=[-2, -1, 0, 1, 2, 7, 8], target=-5) == [1, 6]
