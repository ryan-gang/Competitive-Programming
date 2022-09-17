class Solution:
    """
    Logic :
    # Reverse a base 10 number, with the same logic.
    a, b = 0, 987654321
    while b:
        a = a * 10 + b % 10
        b //= 10
    """

    def reverseBits(self, n: int) -> int:
        ans = 0
        # while n:
        """
        Or the condition can also be this. n will be 0 anyway at the end.
        Nope the condition cannot be this.
        The reverse of 0000...00001 will not be 1, it will be 10000..0000 (32 times.)
        We are supposed to reverse all the bits of a 32 bit uint.
        """
        for _ in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
            # print(ans, n)
        return ans

    # Runtime: 65 ms, faster than 20.62% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 49.28% of Python3 online submissions.
    # Instead of bit manipulations, we are doing calculations with base 2.
    def reverseBitsClever(self, n: int) -> int:
        a = 0
        for _ in range(32):
            a = (a * 2) + (n % 2)
            n //= 2
        return a


sol = Solution()
assert sol.reverseBits(n=43261596) == 964176192
