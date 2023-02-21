class Solution:
    # Runtime: 173 ms, faster than 83.30%.
    # Memory Usage: 23.7 MB, less than 39.30%.
    # T : O(N), S : O(N)
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Logic is pretty simple, we focus on the indices of the array.
        For a segment of the array, where there are only double elements consecutively.
        The double(-th) element will be on an odd index.
        [1, 1, 2, 2, 3, 3, 4, 4] <- VALUES.
        [0, 1, 2, 3, 4, 5, 6, 7] <- INDICES.
        But if there is a single element before the index we are currently on,
        then the double(-th) element will be on an even index.
        We exploit this property and run a binary search.
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 != 0 and nums[mid - 1] == nums[mid]:
                # If mid is odd. Then elements at current and prev index MUST BE SAME.
                # If values match, no anomaly upto here. Look in 2nd half.
                lo = mid + 1
            elif mid < len(nums) - 1 and mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                # If mid is even, then current even and next odd MUST BE SAME.
                # If values match, no anomaly upto here. Look in 2nd half.
                lo = mid + 1
            else:
                # Else. There is anomaly in first half.
                hi = mid - 1

        return nums[lo]

    def singleNonDuplicate1(self, nums: list[int]) -> int:
        """
        We forget about odd and even indices.
        Instead we focus on the partner index of a particular index.
        If idx is odd, it's partner (index with the same value) is odd - 1.
        If idx is even, it's partner is even + 1.
        We can easily calculate the partner index from a given index by XOR-ing with 1.
        odd ^ 1 = odd - 1. (LSB from 1 to 0.)
        even ^ 1 = even - 1. (LSB from 0 to 1.)
        XOR-ing with 1, just reverses the input.
        We just need to check if the partner index and current index has same value.
        And accordingly alter our search space.
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert sol.singleNonDuplicate(nums=[1, 1, 2, 2, 4, 4, 8]) == 8
    assert sol.singleNonDuplicate(nums=[1, 2, 2, 4, 4, 8, 8]) == 1
    assert sol.singleNonDuplicate(nums=[1, 1, 2, 2, 3, 4, 4, 8, 8]) == 3
    assert sol.singleNonDuplicate(nums=[1]) == 1
    assert sol.singleNonDuplicate(nums=[1, 2, 2, 3, 3, 4, 4, 8, 8]) == 1
