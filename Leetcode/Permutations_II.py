from collections import Counter
from typing import Dict, List


class Solution:
    # Runtime: 106 ms, faster than 47.39% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 62.20% of Python3 online submissions.
    # T : O(N x N!), S : O(N!)
    # T : N! factorial permutations, to reach a complete permutation,
    # we need to take N steps, or make N recursive calls.
    # So a loose upper bound is N.N!
    # S : N!, just store all permutations.
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.n = len(nums)
        nums.sort()
        self.traverse(nums, [])
        return self.permutations

    def traverse(self, nums: List[int], permutation: List[int]):
        if len(permutation) == self.n:
            # Do a deep copy here. Because lists are passed as references.
            # So finally we will have empty output, after popping everything.
            self.permutations.append(permutation[::])
        for i in range(len(nums)):
            # Here we are ignoring duplicate elements at each level.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            permutation.append(nums[i])
            self.traverse(nums[:i] + nums[(i + 1):], permutation)
            permutation.pop()

    # Runtime: 99 ms, faster than 54.96% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 78.95% of Python3 online submissions.
    def permute2(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.n = len(nums)
        counter = Counter(nums)
        self.traverseCounter([], counter)
        return self.permutations

    def traverseCounter(self, permutation: List[int], counter: Dict[int, int]):
        if len(permutation) == self.n:
            self.permutations.append(permutation[::])
        for key in counter:
            if counter[key] > 0:
                permutation.append(key)
                counter[key] -= 1
                self.traverseCounter(permutation, counter)
                permutation.pop()
                counter[key] += 1


sol = Solution()
assert (sol.permute2(nums=[1, 2, 3])) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]
assert sol.permute2(nums=[1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
