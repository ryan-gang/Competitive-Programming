class Solution:
    """
    My solutions, do not take advantage of squaring. Other solutions take advantage of squaring,
    which makes the runtime O(logN), so they don't need the threshold checks.
    Apart from that it's okay.
    """

    # Runtime: 1556 ms, faster than 5.65%.
    # Memory Usage: 13.9 MB, less than 67.28%.
    def myPow(self, x: float, n: int) -> float:
        prev, val, threshold = 0, 1, 0.0000000001
        if round(x, 5) == 1.00000:
            return 1
        if round(x, 5) == -1.00000:
            if n % 2:
                return -1
            else:
                return 1
        while n != 0:
            exp = n // abs(n)
            if exp == 1:
                val *= x
            else:
                val /= x
            n -= exp
            if abs(val - prev) < threshold:
                print(val)
                return val
            prev = val
        print(val)
        return val

    def myPow2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        prev, val, threshold = 0, 1, 0.0000000001
        if round(x, 5) == 1.00000:
            return 1
        if round(x, 5) == -1.00000:
            if n % 2:
                return -1
            else:
                return 1
        while n != 0:
            val *= x
            n -= 1
            if abs(val - prev) < threshold:
                return val
            prev = val
        return val

    # Ref : https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
    def myPowRecurse(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPowRecurse(x, n - 1)
        return self.myPowRecurse(x * x, n // 2)

    # Ref : https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
    def myPowIter(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n % 2:
                pow *= x
            x *= x
            n //= 2
        return pow


if __name__ == "__main__":
    sol = Solution()
    assert round(sol.myPow2(x=2.00000, n=10), 5) == 1024.00000
    assert round(sol.myPow2(x=2.10000, n=3), 5) == 9.26100
    assert round(sol.myPow2(x=2.00000, n=-2), 5) == 0.25000
    assert round(sol.myPow2(0.00001, 2147483647), 5) == 0
    assert round(sol.myPow2(1.00000, 2147483647), 5) == 1
    assert round(sol.myPow2(0.99999, 948688), 5) == 0.00008
    assert round(sol.myPow2(-1.00000, 2147483647), 5) == -1
