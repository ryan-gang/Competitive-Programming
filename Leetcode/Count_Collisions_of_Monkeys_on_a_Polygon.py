from functools import lru_cache
from typing import List


class Solution:
    """
    Each monkey can move in the clockwise or counter-clockwise direction,
    so 2 choices for each of n monkeys.
    There are 2 ^ n number of ways.
    If all monkey move in clockwise direction, no collision.
    If all monkey move in counter-clockwise direction, no collision.
    All other ways, collision happens.
    """

    # EZ SOLUTION.
    def monkeyMoveEz(self, n: int) -> int:
        mod = 10**9 + 7
        return (pow(2, n, mod) - 2) % mod

    # Needlessly complicated solution.
    # Reimplementation of pow() with mod.
    def monkeyMove(self, n: int) -> int:
        self.out: List[int] = []
        self.power(2, n, 10**9 + 7)
        return self.out[-1]

    @lru_cache(maxsize=None)
    def power(self, base: int, exp: int, mod: int) -> int:
        if exp == 0:
            return 1
        x = self.power(base, exp // 2, mod)
        x = x * x
        if exp % 2 == 1:
            x = x * base
        self.out.append((x - 2) % mod)
        return x % mod


if __name__ == "__main__":
    sol = Solution()
    assert sol.monkeyMoveEz(500000003) == 1000000006
    assert sol.monkeyMoveEz(55) == 766762394
