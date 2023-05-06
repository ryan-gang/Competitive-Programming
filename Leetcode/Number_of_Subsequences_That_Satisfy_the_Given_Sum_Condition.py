class Solution:
    # Runtime: 803 ms, faster than 87.85%.
    # Memory Usage: 28.6 MB, less than 14.83%.
    # T : O(N), S : O(1)
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        out, mod = 0, 10**9 + 7

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if nums[lo] + nums[hi] <= target:
                out += pow(2, (hi - lo), mod) % mod
                # For elements from lo to hi, all possible subsequences of
                # length 2, will have min + max <= target. So we can take any
                # possible subsequence from the range. But there can be single
                # length subsequences which have a different min and max. So
                # those have to be handled separately then. Instead we put a
                # constraint over the subsequences. The element lo, always has
                # to be taken. And for the other (hi - lo) elements, there are 2
                # ** (hi - lo) possibilities. Of which 1 is an empty
                # subsequence, in that case only the nums[lo] is taken. And for
                # the other cases, nums[lo] is there, and along with it other
                # elements are joined.
                lo += 1
            else:
                hi -= 1

        return out % mod


if __name__ == "__main__":
    sol = Solution()
    assert sol.numSubseq(nums=[3, 5, 6, 7], target=9) == 4
    assert sol.numSubseq(nums=[3, 3, 6, 8], target=10) == 6
    assert sol.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12) == 61
