from functools import lru_cache
from typing import List
from StarterCode.decorators import timeit


# Ref : discuss/1808002/A-very-very-EASY-to-go-EXPLANATION
class Solution:
    """
    The number of bits, for an even number `n` is same as the number of bits in `n/2`,
    the digits are shifted leftwards.
    For an odd number, `n`, the Least significant bit is ALWAYS 1,
    So we take this 1 out, and make it an even number, so its count is count of `n/2` + 1.
    Base case is count(0) = 0, count(1) = 1.
    And we can recurse for the rest, for better time complexity, we can store
    the intermediate values in a dp, and access those later, or use the LRU Cache.
    """

    # Runtime: 185 ms, faster than 34.64% of Python3 online submissions for.
    # Memory Usage: 25.8 MB, less than 29.93% of Python3 online submissions for.
    @timeit
    def countBits(self, n: int) -> List[int]:
        @lru_cache(maxsize=None)
        def count(n):
            if n == 1:
                return 1
            if n & 1:  # n is odd.
                return count(n >> 1) + 1
            else:  # n is even.
                return count(n >> 1)

        out = [0]
        for _ in range(1, n + 1):
            out.append(count(_))
        return out

    # Runtime: 186 ms, faster than 56.23% of Python3 online submissions.
    # Memory Usage: 20.8 MB, less than 79.42% of Python3 online submissions.
    @timeit
    def countBitsDp(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1:  # n is odd.
                dp[i] = dp[i >> 1] + 1
            else:  # n is even
                dp[i] = dp[i >> 1]

        return dp


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBitsDp(1000)[-10:])
