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
        """
        Generate all binary numbers from 0 to 2 ^ nums - 1.
        Which contains all possible combinations of sets, or the power set.
        Then based on the binary representation of a number, we check if ith
        bit is set, if it is set, we add the ith element into that set.
        """
        all_subsets = []
        size = len(nums)
        num_subsets = 1 << size

        for binary in range(num_subsets):
            # print("Binary : ", str(bin(binary)).split("b")[1])
            curr_subset = []
            for digit in range(size):
                val = 1 << digit
                if (val & binary) != 0:
                    curr_subset.append(nums[digit])
            all_subsets.append(curr_subset)

        return all_subsets

    # Runtime: 64 ms, faster than 53.80% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 35.90% of Python3 online submissions.
    def subsets_backtrack(self, nums: List[int]) -> List[List[int]]:
        """
        Here, we are only adding elements after idx, to the array.
        So we do not need to keep track of the added elements.
        """
        self.out, self.nums = [], nums

        def recurse(array, idx):
            self.out.append(array[::])
            for i in range(idx, len(self.nums)):
                array.append(self.nums[i])
                recurse(array, i + 1)
                array.pop()

        recurse([], 0)

        return self.out


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets_bit_manipulation(nums=[1, 2, 3]))
    print(sol.subsets_bit_manipulation(nums=[0]))
