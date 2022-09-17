from typing import List


class Solution:
    nums = []

    # Runtime: 288 ms, faster than 45.39% of Python3 online submissions.
    # Memory Usage: 15.5 MB, less than 65.82% of Python3 online submissions.
    # T : O(N), S : O(1)
    # Still time is not completely optimal, can be improved further.
    # The second part, i.e. the "n" extra zero writes can be done earlier.
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        new_idx, curr_idx = 0, 0

        while curr_idx < len(nums):
            if nums[curr_idx] == 0:
                zero_count += 1
            else:
                nums[new_idx] = nums[curr_idx]
                new_idx += 1
            curr_idx += 1

        idx = len(nums) - zero_count
        while zero_count > 0:
            nums[idx] = 0
            idx += 1
            zero_count -= 1

    # Runtime: 308 ms, faster than 37.05% of Python3 online submissions for Move Zeroes.
    # Memory Usage: 15.6 MB, less than 65.82% of Python3 online submissions for Move Zeroes.
    # T : O(N), S : O(1)
    # We have removed the writing final zeros code.
    # Instead inside the core loop itself we write the old index to 0.
    # Because either it will be overwritten by the actual value, or it
    # will be 0 only. Both ways it is handled correctly.
    # Just do a check that it doesn't overwrite the new index anyway.
    def moveZeroesOptimal(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        new_idx, curr_idx = 0, 0

        while curr_idx < len(nums):
            if nums[curr_idx] == 0:
                zero_count += 1
            else:
                nums[new_idx] = nums[curr_idx]
                if new_idx != curr_idx:
                    nums[curr_idx] = 0
                new_idx += 1
            curr_idx += 1


sol = Solution()
sol.nums = [1]
sol.moveZeroesOptimal(sol.nums)
print(sol.nums)
