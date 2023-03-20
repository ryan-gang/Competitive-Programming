from collections import Counter, defaultdict


class Solution:
    # T : O(N), S : O(N), where N is len(nums)
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        """
        For every num in nums, we find out its "place" in the "required
        sequence". (1, 2, 3, ....). For every num it's smallest possible value
        is num % value. (num = num * value + k, we can repeatedly subtract
        value, to. get k) So, we add the smallest possible form of num to a set,
        if num % value is already there, we add value to it, and get the next
        possible value. And we keep on doing this, num % value, num % value +
        value, num % value + 2*value, ... To, make this process quicker we keep
        the K that needs to be multiplied to each num in a dict. And finally we
        traverse from 1 to MAX, and see which is the smallest number that is
        missing from our set.
        """
        seen: set[int] = set()
        d: dict[int, int] = defaultdict(int)
        for i in nums:
            mod = i % value
            v = d[mod]
            while mod + v in seen:
                v += value
                d[mod] = v
            seen.add(mod + v)

        i, MAX = 0, 10**5
        while i <= MAX:
            if i not in seen:
                return i
            i += 1

        return MAX

    def findSmallestInteger1(self, nums: list[int], value: int) -> int:
        """
        Better version of my solution. The set is removed, and instead in the
        dict itself we keep track of how many num % value we have seen. And then
        while iterating from 1 to MAX, we keep on reducing the number from dict.
        Once a certain num % value reaches 0. That index would be the answer.
        """
        m = Counter([n % value for n in nums])
        for i in range(len(nums)):
            if m[i % value] == 0:
                return i
            m[i % value] -= 1
        return len(nums)

    # Ref : https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
    # solutions/3314226/java-c-python-count-remainders/
    def findSmallestInteger2(self, nums: list[int], value: int) -> int:
        count = Counter(a % value for a in nums)
        stop = 0
        for i in range(value):
            # At the end of the loop, stop will be the key with the lowest value.
            if count[i] < count[stop]:
                stop = i
        # If count[stop] = "l", all the other keys have value AT LEAST "l".
        # So we have "l" complete cycles. 1, 2, 3, ... 1 * value, value + 1 ...
        # 2 * value, 2 * value + 1 .... 3 * value, 3 * value + 1 ..... "l" *
        # value.
        # Our output is of value : atleast value * l. But "stop", the key is
        # derived from doing num % value. This remainder is missing from our
        # output.
        return value * count[stop] + stop


if __name__ == "__main__":
    sol = Solution()
    assert sol.findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=5) == 4
    assert sol.findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=7) == 2
