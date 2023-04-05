from math import ceil


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        At any index `idx`, we can evenly distribute the cumulative sum upto
        `idx` evenly among the indices 0 to `idx`. So, we generate the prefix
        sum upto each index, divided by index we keep this value in our max_val.
        If later on we see a larger max_val we update with that.
        [10, 1, 1] ; We can't distribute 10 evenly among the entire array.
        Which is why max makes sense.
        """
        prefix = 0
        max_val = nums[0]
        for idx, val in enumerate(nums):
            prefix += val
            curr_val = ceil(prefix / (idx + 1))
            max_val = max(max_val, curr_val)
        return max_val


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimizeArrayValue(nums=[3, 7, 1, 6]) == 5
    assert sol.minimizeArrayValue(nums=[10, 1]) == 10
