from operator import xor


class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        max_xor = 0
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i, len(nums)):
                y = nums[j]
                if abs(x - y) <= min(x, y):
                    if xor(x, y) > max_xor:
                        max_xor = xor(x, y)

        return max_xor

    def maximumStrongPairXor1l(self, nums: list[int]) -> int:
        return max(x ^ y for x in nums for y in nums if abs(x - y) <= min(x, y))

    def maximumStrongPairXor2(self, nums: list[int]) -> int:
        max_xor = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j and abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)

        return max_xor
