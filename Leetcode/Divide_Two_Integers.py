class Solution:
    # TLE.
    def divideTLE(self, dividend: int, divisor: int) -> int:
        quotient = 0

        if divisor < 0:
            while dividend >= abs(divisor):
                dividend += divisor
                quotient -= 1
        elif divisor > 0:
            while dividend >= divisor:
                dividend -= divisor
                quotient += 1
        else:
            return 0

        if quotient > 0:
            return min(quotient, 2**31 - 1)
        else:
            return max(-(2**31), quotient)

    # Runtime: 31 ms, faster than 87.46%.
    # Memory Usage: 13.7 MB, less than 97.33%.
    # T : O(N), S : O(N)
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Instead of LINEARLY computing the quotient.
        (If dividend = 10^6 and divisor = 1), this will give TLE.
        Instead we will use bit manipulations to mimic multiplication,
        and do it much faster.
        E.g. 58 = (11) * 5 + 3
        58 = (2 ^ 3 + 2 ^ 1 + 2 ^ 0) * 5 + 3.
        We will try to find the powers of 2 which when added give us the quotient.
        We iterate from 31 to 0, and check if the divisor multiplied by 2 to the
        power of this exponent is greater than the dividend or not.
        If it is greater, then we move on to the smaller exponents.
        Or else we subtract this value (divisor * (2 ^ exp)) from dividend.
        And add (2 ^ exp) to the quotient.
        """
        # Handle special cases
        if dividend == 0:
            return 0
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        sign = (dividend / abs(dividend)) * (divisor / abs(divisor))
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                quotient += 1 << i

        return int(sign * quotient)


if __name__ == "__main__":
    sol = Solution()
    assert sol.divide(10, 3) == 3
    assert sol.divide(7, -3) == -2
    assert sol.divide(-1, 1) == -1
