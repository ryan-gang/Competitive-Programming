class Solution:
    def arraySign(self, nums: list[int]) -> int:
        n = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                n += 1
        return -1 if n % 2 else 1
