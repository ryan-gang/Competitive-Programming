import sys
from typing import List
from loguru import logger

logger.info("Hello loguru!")
logger.add(
    sys.stdout, format="{time} {level} {message}", level="INFO", backtrace=True, diagnose=True
)


class Solution:
    # Runtime: 65 ms, faster than 46.54% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 22.97% of Python3 online submissions.
    # T : O(N x N!), S : O(N!)
    # T : N! factorial permutations, to reach a complete permutation,
    # we need to take N steps, or make N recursive calls.
    # S : N!, just store all permutations.
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.n = len(nums)
        self.permute_array_clean(nums, [])
        return self.permutations

    def permute_array(self, nums: List[int], permutation: List[int]):
        if len(permutation) == self.n:
            self.permutations.append(permutation)
        for i in range(len(nums)):
            self.permute_array(nums[:i] + nums[(i + 1):], permutation + [nums[i]])

    # This is a bit better, instead of creating new lists everytime
    # We are pushing and popping, saving O(N) operations.
    def permute_array_clean(self, nums: List[int], permutation: List[int]):
        if len(permutation) == self.n:
            # Do a deep copy here. Because lists are passed as references.
            # So finally we will have empty output, after popping everything.
            self.permutations.append(permutation[::])
        for i in range(len(nums)):
            permutation.append(nums[i])
            self.permute_array_clean(nums[:i] + nums[(i + 1):], permutation)
            permutation.pop()


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, seen):
            if len(path) == len(nums):
                res.append(path)
                return

            for num in nums:
                if num in path:
                    continue

                seen.add(num)
                dfs(path + [num], seen)

        dfs([], set())
        return res


sol = Solution()
try:
    print(sol.permute(nums=[1, 2, 3]))
except Exception:
    logger.exception("Show me the deets!")
