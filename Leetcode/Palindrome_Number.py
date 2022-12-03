class Solution:
    """
    Just reverse number, and check with original.
    """

    # Runtime: 151 ms, faster than 23.61%.
    # Memory Usage: 13.9 MB, less than 16.27%.
    def isPalindrome(self, x: int) -> bool:
        num = x
        if x < 0:  # Numbers starting with a -
            return False
        rev = 0
        while x:
            rem = x % 10
            x //= 10
            rev = rev * 10 + rem

        print(rev)
        return rev == num


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121)
    assert not sol.isPalindrome(-121)
    assert not sol.isPalindrome(10)
    assert sol.isPalindrome(12345654321)
