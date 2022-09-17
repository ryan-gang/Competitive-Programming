"""
Following is an excerpt form Cracking the Coding Interview book: https://www.careercup.com/book

Our first Instinct in problems like these should be that we're going to have to work with bits.
Why, Because when you take the + sign, what other choice do we have? Plus, that's how computers
do it! Our next thought should be to deeply understand how addition works. We can walk through an
addition problem to see if we can understand something new—some pattern—and then see if we can
replicate that with code. So let, do just that—let, walk through an addition problem. We'll work
in base 10 so that it, easier to see. To add 759 + 674, would usually add digit [0] from each
number, carry the one, add digit [1] from each number, carry the one, and so on. You could take
the same approach in binary: add each digit, and carry the one as necessary. Can we make this a
little easier? Yes! Imagine I decided to split apart the "addition" and "carry" steps. That is,
I do the following:

    Add 759 + 674, but "forget" to carry. I then get 323. Add 759 + 674 but only do the carrying,
    rather than the addition of each digit. I then get 1110. Add the result of the first two
    operations (recursively, using the same process described in step 1 and 2): 1110 + 323 = 1433.

Now, how would we do this in binary?

    If I add two binary numbers together, but forget to carry, the ith bit in the sum will be 0
    only if a and b have the same ith bit (both 0 or both 1).This is essentially an XOR. If I add
    two numbers together but only carry, I will have a 1 in the "ith" bit of the sum only if bits
    "i - 1"th bit of a and b are both 1s. This is an "AND", shifted one place left. Now,
    recurse until there's nothing to carry. """


import random


class Solution:
    # 8 / 25 TC passed. Wrong answer for -1, 1.
    # Stuck in an infinite loop.
    # Some python specific problem.
    # TODO Understand the underlying issue.
    @staticmethod
    def getSum(a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            print(a, b)
            carry = ((a & b) << 1) & mask
            sum = (a ^ b) & mask
            a, b = sum, carry

        return a  # Very clever trick, if `b` is 0, we won’t enter the loop, directly return `a`.


sol = Solution()
assert sol.getSum(-1000, -1000) == -2000
assert sol.getSum(3, 0) == 3
for i in range(10):
    j = random.randint(-1000, -1000)
    k = random.randint(-1000, -1000)
    val = sol.getSum(j, k)
    assert val == j + k, print(f"Sum doesn't match : {j} + {k} = {val}")

assert sol.getSum(-1, 1) == 0
