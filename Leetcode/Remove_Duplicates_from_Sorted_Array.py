# Also present in EPI.
# https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python_solutions/sorted_array_remove_dups.py
from typing import List


class Solution:
    """
    If we are allowed to use extra space, we can use a dictionary, to keep track of dupes,
    and just write the unique elements back to the original array.
    But to optimise it, and not use extra space.
    We can keep track of only the duplicates, we have seen till now. And then if we see a
    new unique element we overwrite the dupes with this. The trick is the next index where
    we should write our unique element is `i - left_shift`,
    where left_shift is the running count of dupes we saw till now.
    """

    # Runtime: 140 ms, faster than 69.40% of Python3 online submissions.
    # Memory Usage: 15.6 MB, less than 66.15% of Python3 online submissions.
    # T : O(N), S : O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        left_shift, n = 0, len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                left_shift += 1
            else:
                write_index = i - left_shift
                nums[write_index] = nums[i]

        return n - left_shift


if __name__ == "__main__":
    sol = Solution()
    assert (sol.removeDuplicates(nums=[1, 2, 3, 3, 3, 4, 4, 5, 6, 7])) == 7
