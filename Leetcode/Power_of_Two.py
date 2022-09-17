class Solution:
    # Runtime: 66 ms, faster than 16.48% of Python3 online submissions for Power of Two.
    # Memory Usage: 13.8 MB, less than 53.53% of Python3 online submissions for Power of Two.
    def isPowerOfTwoRecurse(self, n: int) -> bool:
        # False for everything less than 1, True for 1.
        if n <= 1:
            return n == 1
        if n % 2 == 0:
            return self.isPowerOfTwoRecurse(n / 2)
        return False

    # Runtime: 65 ms, faster than 18.08% of Python3 online submissions for Power of Two.
    # Memory Usage: 13.8 MB, less than 53.53% of Python3 online submissions for Power of Two.
    def isPowerOfTwoIter(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return n == 1

    # Runtime: 38 ms, faster than 84.76% of Python3 online submissions for Power of Two.
    # Memory Usage: 13.9 MB, less than 53.53% of Python3 online submissions for Power of Two.
    # Move the set generation to __init__()
    # def __init__(self) -> None:
    #     self.powers_of_2 = set()
    #     val = 1
    #     for i in range(1, 32):
    #         self.powers_of_2.add(val)
    #         val *= 2
    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n in self.powers_of_2
    def isPowerOfTwoSet(self, n: int) -> bool:
        powers_of_2 = set()
        val = 1
        for i in range(1, 32):
            powers_of_2.add(val)
            val *= 2
        return n in powers_of_2

    # Runtime: 51 ms, faster than 52.90% of Python3 online submissions for Power of Two.
    # Memory Usage: 13.9 MB, less than 9.69% of Python3 online submissions for Power of Two.
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        # If last digit in the binary interpretation is 0
        # That means this number is even.
        while not n & 1:
            # Then we can proceed to divide the number by two.
            n = n >> 1
        return n == 1


sol = Solution()
for val, ans in [
    (-16, False),
    (-8, False),
    (-4, False),
    (-2, False),
    (-1, False),
    (0, False),
    (1, True),
    (2, True),
    (4, True),
    (8, True),
    (16, True),
]:
    assert sol.isPowerOfTwoRecurse(val) == ans, f"Answer wrong for {val}"
    assert sol.isPowerOfTwoIter(val) == ans, f"Answer wrong for {val}"
    assert sol.isPowerOfTwoSet(val) == ans, f"Answer wrong for {val}"
    assert sol.isPowerOfTwo(val) == ans, f"Answer wrong for {val}"
