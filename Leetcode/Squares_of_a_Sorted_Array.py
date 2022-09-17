from typing import List


class Solution:
    # T : O(N), S : O(1)
    def sortedSquaresNaive(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()

        return nums

    # Runtime: 313 ms, faster than 66.23% of Python3 online submissions.
    # Memory Usage: 15.5 MB, less than 99.04% of Python3 online submissions.
    # T : O(N), S : O(1)
    def sortedSquaresNaiveBetter(self, nums: List[int]) -> List[int]:
        n = len(nums)
        flag = False
        if nums[0] < 0:
            flag = True
        for i in range(n):
            nums[i] *= nums[i]
        if flag:
            nums.sort()

        return nums

    # Runtime: 337 ms, faster than 57.87% of Python3 online submissions.
    # Memory Usage: 16.2 MB, less than 49.11% of Python3 online submissions.
    # T : O(N), S : O(N)
    def sortedSquaresX(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [-1] * n
        i = n - 1
        j = 0
        for k in range(n - 1, 0 - 1, -1):
            if abs(nums[i]) >= abs(nums[j]):
                out[k] = nums[i] * nums[i]
                i -= 1
            else:
                out[k] = nums[j] * nums[j]
                j += 1

        return out


sol = Solution()
print(sol.sortedSquares(nums=[-4, -1, 0, 3, 10]))
