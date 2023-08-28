import math


class Solution:
    # Runtime: 4547 ms, faster than 14.17% of Python3 online submissions.
    # Memory Usage: 15.7 MB, less than 45.67% of Python3 online submissions.
    # T : O(N), S : O(N)
    # Uses extra space for creating the final number.
    # We can do better, calculate the decimal inplace.
    def concatenatedBinary1(self, n: int) -> int:
        s = ""
        for i in range(1, n + 1):
            t = bin(i).split("b")[1]
            print(t)
            s += t
        print(s)
        return int(s, 2) % (1000000007)

    # Runtime: 8587 ms, faster than 5.51% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 80.31% of Python3 online submissions.
    # T : O(N), S : O(1)
    # The idea is to use maths to create the sum, based on the previous sum.
    # We are actually doing bit manipulation, without doing bit manipulation explicitly.
    # Based on the current number's length we move the sum,
    # that many digits to the left (multiply or <<).
    # Then we add the current num to sum.
    def concatenatedBinary(self, n: int) -> int:
        sum = 0
        for i in range(1, n + 1, 1):
            length = int(math.log2(i) + 1)
            factor = 2**length
            sum = (sum * factor + i) % (1000000007)

        return sum

    # Ref : https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
    # discuss/2612371/LeetCode-The-Hard-Way-Explained-Line-By-Line
    # the idea is to use bit manipulation to set the current number based on the previous number
    # for example,
    # n = 1, ans = 0b1
    # n = 2 (10), we need to shift 2 bits of the previous ans to the left and add `n`
    # i.e. 1 -> 100 (shift 2 bits to the left) -> 110 (set `10`). ans = 0b110
    # n = 3 (11), we need to shift 2 bits of the previous ans to the left and add `n`
    # i.e 110 -> 11000 (shift 2 bits to the left) -> 11011 (set `11`). ans = 0b11011
    # n = 4 (100), we need to shift 3 bits of the previous ans to the left and add `n`
    # i.e. 11011 -> 11011000 (shift 3 bits to the left) -> 11011100 (set `100). ans = 0b11011100
    # so now we can see a pattern here
    # we need to shift `l` bits of the previous ans to the left and add the current `i`
    # how to know `l`? it is not difficult to see `x` wonly increases when we meet power of 2
    def concatenatedBinaryBinMan(self, n: int) -> int:
        M = 10**9 + 7
        l, ans = 0, 0  # `l` is the bit length to be shifted
        for i in range(1, n + 1):
            # i & (i - 1) means removing the rightmost set bit
            # after removal, if it is 0, then it means it is power of 2
            # as all power of 2 only contains 1 set bit
            # if it is power of 2, we increase the bit length `l`
            if i & (i - 1) == 0:
                l += 1
            # (ans << l) means shifting the orginal answer `l` bits to th left
            # (x | i) means  using OR operation to set the bit
            # e.g. 0001 << 3 = 0001000
            # e.g. 0001000 | 0001111 = 0001111
            ans = ((ans << l) | i) % M
        return ans


sol = Solution()
assert sol.concatenatedBinary(n=1) == 1
assert sol.concatenatedBinary(n=3) == 27
assert sol.concatenatedBinary(n=12) == 505379714
