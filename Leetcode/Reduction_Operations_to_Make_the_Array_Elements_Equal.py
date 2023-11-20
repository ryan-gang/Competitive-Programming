from collections import Counter


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        """
        Every element has to be reduced to the min element, for the `nth`
        element, it needs to go through `n` transformations to become the `0th`
        element. Those `n` moves has to be repeated for all `k` number of the
        `nth` element.
        """
        d = Counter(nums)
        steps = sorted(list(d.keys()))
        i, total_moves = len(steps) - 1, 0

        while i >= 0:
            moves = i * d[steps[i]]
            total_moves += moves
            i -= 1

        return total_moves

    def reductionOperations1(self, nums: list[int]) -> int:
        nums.sort()
        total = steps = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                steps += 1
            # For every unique element increment `steps`
            total += steps
            # For every element add the number of steps (current value is the
            # number of steps it requires to become min) to the total.

        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.reductionOperations(nums=[1, 1, 2, 2, 3]) == 4
    assert sol.reductionOperations(nums=[1, 1, 1]) == 0
    assert sol.reductionOperations(nums=[5, 1, 3]) == 3
