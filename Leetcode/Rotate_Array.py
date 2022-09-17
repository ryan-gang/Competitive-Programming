from typing import List


# Runtime: 383 ms, faster than 32.19% of Python3 online submissions.
# Memory Usage: 25.4 MB, less than 30.16% of Python3 online submissions.
class Solution:
    nums = []

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotation trick :
        nums = "----->-->"; k =3
        result = "-->----->";
        reverse "----->-->" we can get "<--<-----"
        reverse "<--" we can get "--><-----"
        reverse "<-----" we can get "-->----->"
        """
        # Do not return anything, modify nums in-place instead.
        n = len(nums)
        k = k % len(nums)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# n = len(nums)
# k = k % n
# for i in range(len(nums)):
#     j = i
#     prev = nums[j]
#     while(True):
#         old, new = j, j+k % n
#         temp = nums[new]
#         nums[new] = prev


class Solution3:
    # Runtime: 362 ms, faster than 52.43% of Python3 online submissions for Rotate Array.
    # Memory Usage: 25.5 MB, less than 28.43% of Python3 online submissions for Rotate Array.
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        # Very clever, number of total swaps will be exactly equal to len(nums)
        while count < len(nums):
            # start is the starting index, of the swappings.
            current = start
            prev = nums[start]  # store the value in the position
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]  # store it temporarily, to be used in next iteration.
                nums[next] = prev  # overide the next index.
                prev = temp  # reset prev, to keep temp, to be used in next iteration.
                current = next  # Increment index to next.
                count += 1  # Total swaps.

                if start == current:
                    # If after swapping all available elements, we come to "start" again,
                    # exit while loop. This will occur after ALL elements are swapped.
                    break

            start += 1


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=2)
print(Solution.nums)
