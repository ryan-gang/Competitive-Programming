class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return self.get_single_number(nums, K=3)

    def get_single_number(self, nums: list[int], K: int) -> int:
        """
        Given an array of ints, where each element occurs K times, except a lone
        element which occurs only once, return the lone element.

        The way it is done is : For every index in the bit representation of the
        numbers, we count how many times the bit occurs in the entire nums
        array, and then see if the sum is divisible by 3, if it is not divisible
        by 3, that would mean the lone element has this bit set to 1. So we do
        the same to our answer.
        This solution can be easily generalized to any value of K.
        """
        ans = 0

        for exp in range(32):
            mask = 1 << exp
            count = 0
            for num in nums:
                if mask & num:
                    count += 1
            if count % K:  # != 0
                ans |= mask

        if ans & 1 << 31:  # Negative numbers are present.
            ans -= 2**32  # Convert from positive to negative.
        return ans

    def singleNumber1(self, nums: list[int]) -> int:
        """
        (set^val) :
        1. adds `val` to the `set` if `val` is not in the `set` => A^0 = A
        2. removes `val` from the `set` if `val` is already in the `set` => A^A = 0

        Assume `ones` and `twos` to be sets that are keeping track of which
        numbers have appeared once and twice respectively

        `(ones ^ A[i]) & ~twos` basically means perform the above mentioned operation if
        and only if A[i] is not present in the set `twos`.
        So, effectively anything that appears for the first time will be in the
        set. Anything that appears a second time will be removed.

        After this, we immediately update set `twos` as well with similar logic.
        So, effectively, any number that appears a first time will be in set
        `ones` so it will not be added to `twos`. Any number appearing a second
        time would have been removed from set `ones` in the previous step and
        will now be added to set `twos`. Lastly, any number appearing a third
        time will simply be removed from the set `twos` and will no longer exist
        in either set.

        Finally, once we are done iterating over the entire list, set `twos` would be
        empty and set `ones` will contain the only number that appears once.
        """
        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones


if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
    assert sol.singleNumber([0, 1, 0, 1, 0, 1, -99]) == -99
