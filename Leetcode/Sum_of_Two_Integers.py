"""
From CTCI :

To add 759 + 674, would usually add digit [0] from each number, carry the one,
add digit [1] from each number, carry the one, and so on. You could take the
same approach in binary: add each digit, and carry the one as necessary. Can we
make this a little easier? Yes! Imagine I decided to split apart the "addition"
and "carry" steps. That is, I do the following:

    Add 759 + 674, but "forget" to carry. I then get 323. Add 759 + 674 but only
    do the carrying, rather than the addition of each digit. I then get 1110.
    Add the result of the first two operations (recursively, using the same
    process described in step 1 and 2): 1110 + 323 = 1433.

Now, how would we do this in binary?

    If I add two binary numbers together, but forget to carry, the ith bit in
    the sum will be 0 only if a and b have the same ith bit (both 0 or both
    1).This is essentially an XOR. If I add two numbers together but only carry,
    I will have a 1 in the "ith" bit of the sum only if bits "i - 1"th bit of a
    and b are both 1s. This is an "AND", shifted one place left. Now, recurse
    until there's nothing to carry.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while b:
            carry = ((a & b) << 1) & MASK
            sum = (a ^ b) & MASK
            a, b = sum, carry

        return a if a <= MAX else ~(a ^ MASK)


if __name__ == "__main__":
    sol = Solution()
    assert sol.getSum(-1000, -1000) == -2000
    assert sol.getSum(3, 0) == 3
    assert sol.getSum(-1, 1) == 0
