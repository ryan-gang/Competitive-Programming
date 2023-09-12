from functools import cache


# Ref : discuss/1808002/A-very-very-EASY-to-go-EXPLANATION
class Solution:
    """
    The number of bits, for an even number `n` is same as the number of bits in `n/2`,
    the digits are shifted leftwards by 1 place.
    For an odd number, `n`, the Least significant bit is ALWAYS 1,
    So we take this 1 out, and make it an even number, so its count is count of `n/2` + 1.
    Base case is count(0) = 0, count(1) = 1.
    And we can recurse for the rest, for better time complexity, we can store
    the intermediate values in a dp, and access those later, or use the LRU Cache.
    """

    # Runtime: 185 ms, faster than 34.64%.
    # Memory Usage: 25.8 MB, less than 29.93%.
    # T : O(NLogN), S : O(1)
    def countBits(self, n: int) -> list[int]:
        @cache
        def count(n: int) -> int:
            if n == 1:
                return 1
            if n & 1:  # n is odd.
                return count(n >> 1) + 1
            else:  # n is even.
                return count(n >> 1)

        out = [0]
        for val in range(1, n + 1):
            out.append(count(val))
        return out

    # Runtime: 186 ms, faster than 56.23%.
    # Memory Usage: 20.8 MB, less than 79.42%.
    # T : O(N), S : O(1)
    def countBitsDp(self, n: int) -> list[int]:
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
