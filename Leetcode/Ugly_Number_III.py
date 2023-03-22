from math import lcm


class Solution:
    # TLE.
    # Same as Ugly Number II. Except all factors are used, not only prev uglies.
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        new = k = 3
        factors = [a, b, c]
        starts = [1, 1, 1]

        for _ in range(n):
            candidates = [x * y for x, y in zip(factors, starts)]
            new = min(candidates)
            for idx in range(k):
                if candidates[idx] == new:
                    starts[idx] += 1
        return new

    # Runtime: 38 ms, faster than 25.30%.
    # Memory Usage: 14 MB, less than 37.5%.
    # T : O(LogN), S : O(1)
    def nthUglyNumber1(self, n: int, a: int, b: int, c: int) -> int:
        def is_enough(number: int, a: int, b: int, c: int) -> int:
            """
            If number is enough to contain n multiples of a, b, c return True.
            """
            ab, bc, ca, abc = lcm(a, b), lcm(b, c), lcm(c, a), lcm(a, b, c)

            A, B, C, AB, BC, CA, ABC = (
                number // a,
                number // b,
                number // c,
                number // ab,
                number // bc,
                number // ca,
                number // abc,
            )
            return A + B + C - AB - BC - CA + ABC >= n

        # Binary search from hi to lo.
        # hi is set to min(a,b,c) * n
        # For the smallest factor if we have n multiples, we are bound to have
        # more than or equal to n multiple for all factors together.
        k = min(a, b, c)
        hi = k * n
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            enough = is_enough(mid, a, b, c)
            if enough:
                hi = mid
            else:
                lo = mid + 1

        return lo
