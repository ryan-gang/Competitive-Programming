from collections import deque
from typing import List


class Solution:
    # Runtime: 543 ms, faster than 74.85% of Python3 online submissions.
    # Memory Usage: 21 MB, less than 38.01% of Python3 online submissions.
    # T : O(N^2), S : O(N)
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        Create monotonic decreasing stack. With vals, and indices.
        If curr is > than stack.peek() see if greater than other elements in stack.
        """
        stack = deque()
        max_ramp = 0
        stack.append((0, nums[0]))
        for idx, num in enumerate(nums):
            # No need to check if stack is valid.
            # We are never gonna pop from stack, and we init it with some seed data.
            if num < stack[-1][1]:
                stack.append((idx, num))
            else:
                """
                If the num in nums, is greater than our top element in stack, we try to find what
                is the biggest number in the stack, which is smaller than num and
                then find the max_ramp for num.
                We can actually use binary search here, to improve runtime to O(logN) from O(N).
                """
                ramp = 0
                for i in range(len(stack) - 1, -1, -1):
                    lower_idx, lower_num = stack[i]
                    if num >= lower_num:
                        ramp = idx - lower_idx
                        max_ramp = max(ramp, max_ramp)
                    else:
                        break

        return max_ramp

    # Runtime: 523 ms, faster than 75.73% of Python3 online submissions for Maximum Width Ramp.
    # Memory Usage: 20.9 MB, less than 58.19% of Python3 online submissions for Maximum Width Ramp.
    # T : O(N), S : O(N)
    def maxWidthRamp2(self, nums):
        stack = []
        res = 0
        # In this loop we create a monotonic decreasing stack.
        for idx, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(idx)

        # We iterate over the nums array from the end to start.
        for j in range(len(nums))[::-1]:
            """
            If the top element in the stack (Last-Inserted), is smaller than nums[j]
            (from the end of nums), it should be understood that this is the highest ramp possible
            for the stack[-1], becuase
            nums[j] is furthest from it, all successive elements will be nearer to it,
            thus smaller ramp. So we can pop it.
            Res would contain the ramp length data for it.
            """
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxWidthRamp(nums=[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
    assert sol.maxWidthRamp(nums=[6, 0, 8, 2, 1, 5]) == 4
    assert sol.maxWidthRamp(nums=[6, 0, 8, 2, 1, 5]) == 4
    assert sol.maxWidthRamp(nums=[6, 5, 4, 3, 2, 1]) == 0
    assert sol.maxWidthRamp(nums=[6, 1]) == 0
    assert sol.maxWidthRamp(nums=[6, 6, 6, 6, 6]) == 4
