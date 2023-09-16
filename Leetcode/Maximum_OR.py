class Solution:
    """
    For every num in the nums array, we will multiply num by 2^k, and keep a
    track of the bitwise OR of all the array elements taken together. To perform
    this computation optimally, we keep a prefix and a suffix array.

    prefix[i] = bitwise OR of elements at index 0 to i-1.
    suffix[i] = bitwise OR of elements at index i+1 to n-1.
    The reason why we are multiplying a single element by 2^k instead of
    multiple elements is simple. If we spread out the k over multiple elements,
    our max OR will not be multiplied by the most optimal multiplicative factor
    that it could have been.
    """

    # T : O(N), S : O(N)
    def maximumOr(self, nums: list[int], k: int) -> int:
        # prefix array.
        # prefix[i] = bitwise OR of elements from index 0 to i-1.
        pre = [0]
        or_val = 0
        for num in nums:
            or_val |= num
            pre.append(or_val)
        pre.pop()

        # suffix array.
        # suffix[i] = bitwise OR of elements from index i+1 to n-1.
        suf = [0]
        or_val = 0
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            or_val |= num
            suf.append(or_val)
        suf.pop()
        suf.reverse()

        # Then we iterate over the nums array
        # Multiply every num by 2^k
        # And see how it would affect the overall OR
        # And keep the max OR.
        max_or = 0
        for idx in range(len(nums)):
            num = nums[idx] << k
            prefix = pre[idx]
            suffix = suf[idx]

            max_or = max(max_or, num | prefix | suffix)

        return max_or
