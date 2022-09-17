class Solution:
    # Runtime: 44 ms, faster than 69.12% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 10.18% of Python3 online submissions.
    def isPowerOfFour(self, n: int) -> bool:
        # While n > 0, first check if it is less equal to 0, or equal to 1.
        # Then check if the last 2 digits of the number are 0.
        # If that is the case, divide n by 4, and continue loop.
        # Else return False.
        while n:
            if n <= 0:
                return False
            if n == 1:
                return True
            if not ((n & (1 << 0)) | (n & (1 << 1))):
                n = n >> 2
            else:
                return False
        return False

    # Runtime: 137 ms, faster than 5.37% of Python3 online submissions.
    # Memory Usage: 14.3 MB, less than 10.18% of Python3 online submissions.
    def isPowerOfFourRecurse(self, n: int) -> bool:
        # False for everything less equal to 0.
        if n <= 0:
            return False
        # If n has reached exact 1, return True.
        elif n == 1:
            return True
        # Else call isPowerOfFour with n divided by 4.
        return self.isPowerOfFourRecurse(n / 4)


sol = Solution()
for i in range(-10, 256 * 17):
    if sol.isPowerOfFour(i):
        print(f"{i} : {sol.isPowerOfFour(i)}")
