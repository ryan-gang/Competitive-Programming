class Solution:
    # T : O(N), S : O(1)
    # Kadane's Algo.
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = add = 0
        for val in nums:
            add += val
            max_sum = max(add, max_sum)
            # This line being first means we get the lowest negative value too,
            # if we get add as 0, 0 becomes the lower ceiling for our answer.
            add = max(0, add)

        return max_sum


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([-1]) == -1
