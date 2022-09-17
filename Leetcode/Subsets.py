from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output

    # Different implementation of the cascading algo.
    def subsets_cascading(self, nums):
        all = [[]]
        for num in nums:
            all_loop = []
            for subset in all:
                curr = subset[::]
                curr.append(num)
                all_loop.append(curr)

            all.extend(all_loop)

        return all

    # Runtime: 73 ms, faster than 9.49%.
    # Memory Usage: 14.1 MB, less than 82.18%.
    def subsets_bit_manipulation(self, nums):
        all_subsets = []
        size = len(nums)
        num_subsets = 1 << size

        for binary in range(num_subsets):
            # print(str(bin(binary)).split("b")[1])
            curr_subset = []
            for digit in range(size):
                val = 1 << digit
                if (val & binary) != 0:
                    curr_subset.append(nums[digit])
            all_subsets.append(curr_subset)

        return all_subsets

    # Runtime: 62 ms, faster than 28.24%.
    # Memory Usage: 14.2 MB, less than 35.74%.
    def subsets_backtrack(self, nums):
        self.nums, self.all = nums, [[]]

        def dfs(curr, index):
            for i in range(index, len(nums)):
                curr.append(nums[i])
                self.all.append(curr[::])
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return all


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets_cascading(nums=[1, 2, 3]))
