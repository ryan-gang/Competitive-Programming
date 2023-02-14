class Solution:
    """
    Assume n is on the board, n % (n - 1) == 1 if n > 2,
    so n - 1 will be on the board, then n - 2 will be on the board,
    similarly, n - 3, n - 4 .... 3, 2.
    So for any n > 1,
    2, 3, 4... n will be on the board eventually, so we return n - 1.
    But, for n = 1 nothing will happen, no number that is 1 <= 1 <= 1. Only 1.
    So, we return 1.
    """

    # Runtime: 27 ms, faster than 90.95%.
    # Memory Usage: 14 MB, less than 7.97%.
    # T : O(1), S : O(1)
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return n
        return n - 1
