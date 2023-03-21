class Solution:
    # Runtime: 1087 ms, faster than 78.8%.
    # Memory Usage: 24.5 MB, less than 78.9%.
    # T : O(N), S : O(1)
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        curr is the number of subarrays ending at the current index. If the next
        index is also 0, we can increment all the subarrays with the next index,
        and additionally create a new subarray with only the next index. But on
        encountering a non-zero int, this streak breaks.
        """
        total = curr = 0
        for num in nums:
            if num == 0:
                curr += 1
                total += curr
            else:
                curr = 0

        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]) == 9
    assert sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert sol.zeroFilledSubarray([2, 10, 2019]) == 0
