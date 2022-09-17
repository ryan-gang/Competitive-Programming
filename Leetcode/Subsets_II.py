from typing import List


class Solution:
    def helper(self, nums):
        all = [[]]

        def dfs(curr, index):
            for i in range(index, len(nums)):
                curr.append(nums[i])
                if curr[::] not in all:
                    all.append(curr[::])
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return all

    # Runtime: 63 ms, faster than 42.19%.
    # Memory Usage: 14.2 MB, less than 49.17%.
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.nums.sort()
        self.all = [[]]

        def dfs(curr, index):
            for i in range(index, len(self.nums)):
                """One of the duplicates, HAS to be processed.
                As we start the loop from `index`.
                we will always process that, no matter what.
                This is where our loop also starts.
                This can be assumed to be unique.
                Then from the very next element we start checking for and skipping duplicates."""
                if i > index and self.nums[i] == self.nums[i - 1]:
                    continue
                curr.append(self.nums[i])
                self.all.append(curr[::])
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return self.all
