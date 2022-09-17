class Solution:
    """
    The tricky part of this problem is to find the prefix pattern.
    For example, for number 26 to 30
    Their binary form are:
    11010
    11011
    11100
    11101
    11110
    Because we are trying to find bitwise AND, so if there is any bit which is 0,
    that bit in the answer will then be 0.
    Like in this case, it is 11000.
    So we are go to cut all these bit that they are different. In this case we cut the right 3 bit.
    So it's like finding the "common prefix" of m and n 's binary code.
    """

    # Runtime: 84 ms, faster than 67.21% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 69.03% of Python3 online submissions.
    # T : O(N), S : O(1)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        factor = 0
        # Until right and left are same, we keep on trimming the right most bits.
        # And counting the number of bits trimmed.
        # We return the trimmed result.
        while right != left:
            left = left >> 1
            right = right >> 1
            factor += 1
        return left << factor


sol = Solution()
assert sol.rangeBitwiseAnd(left=5, right=7) == 4
assert sol.rangeBitwiseAnd(left=0, right=0) == 0
assert sol.rangeBitwiseAnd(left=1, right=2147483647) == 0
# Ref : https://leetcode.com/problems/bitwise-and-of-numbers-range/
# discuss/56729/Bit-operation-solution(JAVA)
