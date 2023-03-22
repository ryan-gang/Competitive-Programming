class Solution:
    """
    Repeatedly divide the number by 2, 3, 5. As long as it is divisible.
    After all the divisions if we reach 1, n was of the form 2^J * 3 ^K * 5^L.
    """

    # Runtime: 56 ms, faster than 64.11%.
    # Memory Usage: 13.9 MB, less than 12.18%.
    def isUgly(self, n: int) -> bool:
        if n > 0:
            for prime in [2, 3, 5]:
                while n % prime == 0:
                    n //= prime
        return n == 1

    # Runtime: 61 ms, faster than 49.68%.
    # Memory Usage: 13.8 MB, less than 59.97%.
    def isUgly2(self, n: int) -> bool:
        if n <= 0:
            return False
        while not (n % 3):
            n //= 3
        while not (n % 5):
            n //= 5
        return n & n - 1 == 0  # Check if n is of the form 2 ^ X.


if __name__ == "__main__":
    sol = Solution()
    assert sol.isUgly2(30)
    assert sol.isUgly2(6)
    assert sol.isUgly2(1)
    assert not (sol.isUgly2(14))
    assert not (sol.isUgly2(0))
    assert not (sol.isUgly2(-14))
    assert not (sol.isUgly2(-1))
