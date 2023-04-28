from math import sqrt


class Solution:
    """
    Initially all bulbs are off.
    Then for every natural number, we invert all the bulbs which are multiples
    of the current number. In this way, every number that is not a perfect
    square has an even number of factors, so it gets flipped an even number of
    times. (Finally turned off.) On the other hand perfect square numbers are
    flipped an odd number of times. So the final answer is just the number of
    perfect squares from 1 to n.
    """

    def bulbSwitch(self, n: int) -> int:
        # Not required, we just need sqrt(n).
        i = 1
        count = 0
        while i * i <= n:
            count += 1
            i += 1

        return count

    def bulbSwitch1(self, n: int) -> int:
        return int(sqrt(n))
