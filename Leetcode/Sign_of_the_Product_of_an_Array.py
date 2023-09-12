class Solution:
    # T : O(N), S : O(1)
    def arraySign(self, nums: list[int]) -> int:
        sign = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign += 1
        return -1 if sign % 2 else 1
