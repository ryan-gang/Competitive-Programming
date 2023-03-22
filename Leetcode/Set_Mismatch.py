class Solution:
    # T : O(N), S : O(1)
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        In the nums array, we negate all the indices. If some indice is already
        negative, this would be the repeated val. And the one not negated is the
        missing one.
        """
        dup, missing = -1, -1
        for idx, val in enumerate(nums):
            index_for_val = val - 1
            # If index is already negative, we can be sure this value is the dupe.
            if nums[index_for_val] < 0:
                dup = abs(val)
            # Else we multiply index with -1.
            else:
                nums[index_for_val] *= -1

        # If val is positive, then the corresponding value is missing.
        for idx, val in enumerate(nums):
            if val > 0:
                missing = idx + 1

        return [dup, missing]

    # T : O(N), S : O(N)
    def findErrorNums1(self, nums: list[int]) -> list[int]:
        # 1 liner. Based on summation of the array, against the expected value.
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]
